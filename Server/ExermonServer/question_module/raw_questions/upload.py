from django.core.files import File
from utils.exception import ErrorType, GameException
from question_module.models import QuestionType
import os, json, re, random, traceback

def doPreprocess():
	questions = []

	for sub_id in range(9):
		try:
			with open('subject_%d.que' % (sub_id + 1), 'r', encoding='utf-8') as file:
				data = file.read()
				data = json.loads(data)

				print("Loading " + data['subject'])

				questions.extend(processData(sub_id, data))
		except:
			traceback.print_exc()

	return questions


def processData(subject_id, data):
	questions = []

	total = len(data['data'])
	cnt = 1

	for d in data['data']:
		try:
			print("    Loading %d/%d :%s" % (cnt, total, d['title'][:10]))
			questions.append(processQuestion(subject_id, d))

		except Exception as e:
			traceback.print_exc()

		cnt += 1

	return questions


def processQuestion(subject_id, question):
	question['subjectId'] = subject_id
	question['title'] = processTitle(question['title'])
	question['level'] = processLevel(question['level'])
	question['choices'] = processChoices(question['choices'])

	if 'description' in question:
		question['description'] = processDescription(question['description'])
	else:
		question['description'] = '无'

	if 'pictures' in question:
		question['pictures'] = processPictures(question['pictures'])
	else:
		question['pictures'] = []

	if 'type' not in question:
		question['type'] = processType(question['choices'])

	if 'score' not in question:
		question['score'] = 6

	return question


def processTitle(title):
	reg = r'\d+． *'
	title = re.sub(reg, '', title)
	return processCommonText(title)


def processDescription(description):
	return processCommonText(description)


def processLevel(level):
	if isinstance(level, int):
		return level
	else:
		reg = r'\d\.\d+'
		r = re.search(reg, level)
		r = float(r.group(0))
		if r >= 0.9: return random.randint(0, 1)
		if r >= 0.8: return random.randint(1, 2)
		if r >= 0.7: return random.randint(2, 3)
		if r >= 0.6: return random.randint(3, 4)
		if r >= 0.5: return random.randint(4, 5)
		return 5


def processChoices(choices):
	reg = r'[A-Z]． *'
	for choice in choices:
		choice['text'] = re.sub(reg, '', choice['text'])
		choice['text'] = processCommonText(choice['text'])
	return choices


def processType(choices):
	cnt = 0

	for choice in choices:
		if choice['ans']:
			cnt += 1

	if cnt <= 0:
		raise GameException(ErrorType.QuestionNoAnswer)

	if cnt == 1: return QuestionType.Single
	if cnt > 1: return QuestionType.Multiple

	return QuestionType.Other


def processPictures(pictures):
	files = []
	for picture in pictures:
		files.append(File(open('/' + picture, 'rb')))

	return files


def processCommonText(text):
	# flireg = r'</?(br|a|div|em|label|span|table|td|font|tbody|tr|img|!--).*?/?>'
	# ulreg = r'<bdo.*?>(?P<cont>.*?)</bdo>'
	# text = re.sub(ulreg, underline, text)
	# text = re.sub(flireg, '', text)
	return text

# def underline(matched):
# 	cont = str(matched.group('cont'))
# 	return '【'+cont+'】'