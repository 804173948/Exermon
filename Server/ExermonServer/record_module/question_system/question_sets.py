from django.db import models

from ..types import *
from ..manager import RecordManager

import record_module.models as Models

from utils.calc_utils.question_calc import *


# ===================================================
#  刷题记录表
# ===================================================
class BaseExerciseRecord(Models.QuesSetRecord):

	# 常量定义
	NAME_STRING_FMT = "%s\n%s %s"

	# 科目
	subject = models.ForeignKey('game_module.Subject', on_delete=models.CASCADE,
								verbose_name="科目")

	# 题量（用于生成题目）
	count = models.PositiveSmallIntegerField(default=1, verbose_name="题量")

	# 所属赛季
	season = models.ForeignKey('season_module.CompSeason', on_delete=models.CASCADE,
							   verbose_name="所属赛季")

	# 生成名字
	def _nameParams(self):
		create_time = ModelUtils.timeToStr(self.create_time)
		verbose_name = type(self)._meta.verbose_name

		return create_time, self.subject.name, verbose_name

	def _convertBaseInfo(self, res, type):
		super()._convertBaseInfo(res, type)

		res['season_id'] = self.season_id
		res['subject_id'] = self.subject_id
		res['count'] = self.count

	# 开始刷题
	def _create(self, subject, count):
		super()._create()

		from season_module.runtimes import SeasonManager

		self.season_id = SeasonManager.getCurrentSeason().id
		self.subject = subject
		self.count = count

	# 生成题目生成配置信息
	def _makeGenerateConfigure(self, **kwargs):
		return BaseQuestionGenerateConfigure(
			self, self.exactlyPlayer(), self.subject, self.count)

	def _shrinkQuestions(self):
		"""
		压缩题目，用于排除未作答的题目，通过移除缓存题目的方式实现
		"""

		player_queses = self.playerQuestions()
		player_queses = list(player_queses).copy()

		for player_ques in player_queses:
			if not player_ques.answered:
				self._removeQuestion(player_ques)

	# 终止答题
	def terminate(self, **kwargs):
		self._shrinkQuestions()
		super().terminate(**kwargs)


# region 刷题

# ===================================================
#  刷题记录表
# ===================================================
@RecordManager.registerQuestionSet("刷题记录",
	GeneralQuestionGenerator, ExerciseResultRewardCalc)
class GeneralExerciseRecord(BaseExerciseRecord):

	# 最大刷题数
	MAX_COUNT = 10

	GEN_TYPES = [
		(QuestionGenerateType.Normal.value, '普通模式'),
		(QuestionGenerateType.OccurFirst.value, '已做优先'),
		(QuestionGenerateType.NotOccurFirst.value, '未做优先'),
		(QuestionGenerateType.WrongFirst.value, '错题优先'),
		(QuestionGenerateType.CollectedFirst.value, '收藏优先'),
		(QuestionGenerateType.SimpleFirst.value, '简单题优先'),
		(QuestionGenerateType.MiddleFirst.value, '中等题优先'),
		(QuestionGenerateType.DifficultFirst.value, '难题优先'),
	]

	# 题目分配模式
	gen_type = models.PositiveSmallIntegerField(choices=GEN_TYPES,
												default=QuestionGenerateType.Normal.value,
												verbose_name="生成模式")

	def _convertBaseInfo(self, res, type):
		super()._convertBaseInfo(res, type)

		res['gen_type'] = self.gen_type

	# 开始刷题
	def _create(self, subject, count, gen_type=QuestionGenerateType.Normal.value):
		super()._create(subject, count)

		self.gen_type = gen_type

	# 生成题目生成配置信息
	def _makeGenerateConfigure(self, **kwargs):
		return GeneralQuestionGenerateConfigure(
			self, self.exactlyPlayer(), self.subject,
			gen_type=self.gen_type, count=self.count)

	def selections(self, player_queses=None) -> list:
		"""
		获取每道题目的选择情况
		Args:
			player_queses (QuerySet): 玩家题目关系集合，默认情况下为所有题目关系
		Returns:
			题目选择情况列表
		"""
		return self._totalData('selections',
							   lambda d: d.selection, player_queses)


# ===================================================
#  刷题奖励表
# ===================================================
@RecordManager.registerQuestionSetReward(GeneralExerciseRecord)
class ExerciseReward(Models.QuesSetReward): pass

# endregion

# region 听力题


# ===================================================
#  听力题目记录表
# ===================================================
@RecordManager.registerQuestionSet("听力题记录",
	RandomQuestionGenerator)
class ListeningExerciseRecord(BaseExerciseRecord): pass


# ===================================================
#  听力题目记录表
# ===================================================
@RecordManager.registerQuestionSetReward(ListeningExerciseRecord)
class ListeningExerciseReward(Models.QuesSetReward): pass


# endregion

# region 阅读题


# ===================================================
#  听力题目记录表
# ===================================================
@RecordManager.registerQuestionSet("阅读题记录",
	RandomQuestionGenerator)
class ReadingExerciseRecord(BaseExerciseRecord): pass


# ===================================================
#  听力题目记录表
# ===================================================
@RecordManager.registerQuestionSetReward(ListeningExerciseRecord)
class ReadingExerciseReward(Models.QuesSetReward): pass


# endregion

# region 单词题


# ===================================================
#  听力题目记录表
# ===================================================
@RecordManager.registerQuestionSet("单词题记录",
	RandomQuestionGenerator)
class WordExerciseRecord(Models.QuesSetRecord):

	DEFAULT_COUNT = 50

	# 题量（用于生成题目）
	count = models.PositiveSmallIntegerField(
		default=DEFAULT_COUNT, verbose_name="题量")

	def _convertBaseInfo(self, res, type):
		super()._convertBaseInfo(res, type)

		res['count'] = self.count

	# 开始刷题
	def _create(self, count=DEFAULT_COUNT, **kwargs):
		super()._create()
		self.count = count


# ===================================================
#  听力题目记录表
# ===================================================
@RecordManager.registerQuestionSetReward(ListeningExerciseRecord)
class WordExerciseReward(Models.QuesSetReward): pass


# endregion

# region 短语题


# ===================================================
#  听力题目记录表
# ===================================================
@RecordManager.registerQuestionSet("短语题记录",
	RandomQuestionGenerator)
class PhraseExerciseRecord(Models.QuesSetRecord):

	DEFAULT_COUNT = 10

	# 题量（用于生成题目）
	count = models.PositiveSmallIntegerField(
		default=DEFAULT_COUNT, verbose_name="题量")

	def _convertBaseInfo(self, res, type):
		super()._convertBaseInfo(res, type)

		res['count'] = self.count

	# 开始刷题
	def _create(self, count=DEFAULT_COUNT, **kwargs):
		super()._create()
		self.count = count


# ===================================================
#  听力题目记录表
# ===================================================
@RecordManager.registerQuestionSetReward(ListeningExerciseRecord)
class PhraseExerciseReward(Models.QuesSetReward): pass


# endregion