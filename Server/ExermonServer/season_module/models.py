from django.db import models
from utils.model_utils import Common as ModelUtils
from game_module.models import GroupConfigure
from player_module.views import Common
from player_module.models import Player
import datetime

# Create your models here.


# =======================
# 赛季记录表
# =======================
class SeasonRecord(models.Model):

	class Meta:
		verbose_name = verbose_name_plural = "赛季记录"

	SUSPEN_SCORE = 50

	# 玩家
	player = models.ForeignKey('player_module.Player', on_delete=models.CASCADE, verbose_name="玩家")

	# 赛季
	season = models.ForeignKey('CompSeason', on_delete=models.CASCADE, verbose_name="赛季")

	# 赛季积分
	point = models.PositiveSmallIntegerField(default=0, verbose_name="赛季积分")

	# 段位星星
	star_num = models.PositiveSmallIntegerField(default=0, verbose_name="段位星星")

	def convertToDict(self):
		suspensions = ModelUtils.objectsToDict(self.suspensions())

		return {
			'id': self.id,
			'player_id': self.player,
			'season_id': self.season,
			'star_num': self.star_num,
			'point': self.point,

			'suspensions': suspensions,
		}

	# 增减赛季积分
	def adjustPoint(self, value):
		self.point = max(self.point+value, 0)

		self.save()

	# 增减星星数量
	async def adjustStarNum(self, value):
		rank, sub_rank = self.rank()

		# 星星减少
		while value < 0:
			# 当前段位赛季积分和抵消因子
			self.point -= rank.offset_factor
			value += 1

			# 情况1，赛季积分不够完全抵消，point用完，此时value<0，段位可能改变
			if self.point < 0:
				self.point += rank.offset_factor
				value -= 1
				break

		# 情况2，赛季积分可以完全抵消星星减少数，args提前变为0，段位不变
		# 情况3，星星数增加，段位可能改变
		if value != 0:
			self.star_num += value
			new_rank, new_sub_rank = self.rank()
			if new_rank != rank or new_sub_rank != sub_rank:
				await self._emitRankChanged(new_rank, new_sub_rank)

		self.save()

	# 发送段位变更信息
	async def _emitRankChanged(self, rank, sub_rank):
		from game_module.consumer import EmitType

		# 生成返回信息，规范见接口文档
		data = {'rank_id': rank, 'sub_rank': sub_rank, 'star_num': self.star_num}

		player = Common.getOnlinePlayer(self.player_id)
		# 使用 emit 函数发送信息，type 为发送信息的类型，
		# tag 为发送信息的标签（按照默认值即可）
		# data 为发送的信息，需要传一个 dict
		await player.consumer.emit(EmitType.RankChanged, data=data)

	def adjustCredit(self, player: Player, credit):
		player.credit += credit

		count = self.suspensions().count()
		now = datetime.datetime.now()

		# 针对第1，2，>=3次禁赛，分别设置3，7，30天的禁赛期
		if player.credit < self.SUSPEN_SCORE and count >= 2:
			SuspensionRecord.create(self.id, now, 30)

		elif player.credit < self.SUSPEN_SCORE and count == 1:
			SuspensionRecord.create(self.id, now, 7)

		elif player.credit < self.SUSPEN_SCORE and count == 0:
			SuspensionRecord.create(self.id, now, 3)

		player.save()

	# 所有的禁赛纪录
	def suspensions(self):
		return self.suspensionrecord_set.all()

	def isBanned(self) -> bool:
		"""
		当前是否禁赛
		Returns:
			返回是否禁赛
		"""
		now = datetime.datetime.now()
		suspensions = self.suspensions()

		for susp in suspensions:
			if susp.start_time <= now < susp.end_time:
				return True

		return False

	def rank(self) -> ('CompRank', int):
		"""
		计算当前实际段位
		Returns:
			返回实际段位对象（CompRank）和子段位数目（从0开始）
		"""
		# ranks 储存了段位列表中的每一个段位的详细信息
		ranks = CompRank.objs()

		# 每个段位需要的星星数量相加
		sum = 0

		for rank in ranks:
			rank_stars = rank.rankStars()

			# 如果段位是无限累计 或 星星数不足以进入下一段位
			if rank_stars == 0 or self.star_num < sum+rank_stars:
				# 计算子段位（还是从 0 开始计算吧）
				sub_rank = (self.star_num-sum) / CompRank.STARS_PER_SUBRANK

				return rank, sub_rank

			sum += rank_stars

		return None, 0


# =======================
# 禁赛记录表
# =======================
class SuspensionRecord(models.Model):

	class Meta:
		verbose_name = verbose_name_plural = "禁赛记录"

	# 赛季记录,一对多的关系，多个禁赛记录对应一个赛季记录
	season_rec = models.ForeignKey('SeasonRecord', on_delete=models.CASCADE,
								   verbose_name="赛季记录")

	# 开始时间
	start_time = models.DateTimeField(auto_now_add=True, verbose_name="开始时间")

	# 结束时间
	end_time = models.DateTimeField(verbose_name="结束时间")

	# 创建一个实例，cls 可以直接当做 SuspensionRecord 来用
	@classmethod
	def create(cls, season_rec, start_time, time_length):
		record = cls()
		record.season_rec = season_rec
		record.start_time = start_time
		record.end_time = start_time + datetime.timedelta(days=time_length)

		record.save()

		return record

	def convertToDict(self):
		start_time = ModelUtils.timeToStr(self.start_time)
		end_time = ModelUtils.timeToStr(self.end_time)

		return {
			'start_time': start_time,
			'end_time': end_time
		}


# =======================
# 赛季配置表
# =======================
class CompSeason(GroupConfigure):

	class Meta:
		verbose_name = verbose_name_plural = "赛季信息"

	# 开始时间
	start_time = models.DateTimeField(verbose_name="开始时间")

	# 结束时间
	end_time = models.DateTimeField(verbose_name="结束时间")

	def convertToDict(self):
		res = super().convertToDict()

		start_time = ModelUtils.timeToStr(self.start_time)
		end_time = ModelUtils.timeToStr(self.end_time)

		res['start_time'] = start_time
		res['end_time'] = end_time

		return res


# =======================
# 段位配置表
# =======================
class CompRank(GroupConfigure):

	class Meta:
		verbose_name = verbose_name_plural = "段位信息"

	# 每个小段位所需星星数
	STARS_PER_SUBRANK = 3

	# 颜色
	color = models.CharField(max_length=7, null=False,
							 default='#000000', verbose_name="颜色")

	# 子段位数（0 为无限）
	sub_rank_num = models.PositiveSmallIntegerField(default=3, verbose_name="小段位数")

	# 积分因子
	score_factor = models.PositiveSmallIntegerField(default=80, verbose_name="积分因子")

	# 抵消积分
	offset_factor = models.PositiveSmallIntegerField(default=60, verbose_name="抵消使用积分")

	# 管理界面用：显示星级颜色
	def adminColor(self):
		from django.utils.html import format_html

		res = '<div style="background: %s; width: 48px; height: 24px;"></div>' % self.color

		return format_html(res)

	adminColor.short_description = "星级颜色"

	def convertToDict(self):
		res = super().convertToDict()

		res['color'] = self.color
		res['sub_rank_num'] = self.sub_rank_num
		res['score_factor'] = self.score_factor
		res['offset_factor'] = self.offset_factor

		return res

	# 计算每个段位需要的星星数量
	def rankStars(self):
		return self.sub_rank_num * self.STARS_PER_SUBRANK
