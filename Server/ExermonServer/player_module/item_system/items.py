from item_module.manager import *
from item_module.models import *

# import player_module.item_system.cont_items as ContItems
# from . import *


# ===================================================
#  人类物品使用效果表
# ===================================================
class GameItemEffect(BaseEffect):

	class Meta:
		verbose_name = verbose_name_plural = "人类物品使用效果"

	# 物品
	item = models.ForeignKey('player_module.GameItem', on_delete=models.CASCADE,
							 verbose_name="物品")


# ===================================================
#  人类物品价格
# ===================================================
class GameItemPrice(Currency):

	class Meta:
		verbose_name = verbose_name_plural = "人类物品价格"

	LIST_DISPLAY_APPEND = ['item']

	# 物品
	item = models.OneToOneField('player_module.GameItem', on_delete=models.CASCADE,
								verbose_name="物品")


# ===================================================
#  人类物品表
# ===================================================
@ItemManager.registerItem("一般道具")
class GameItem(UsableItem):

	# 获取所有的效果
	@CacheHelper.staticCache
	def effects(self):
		return self.gameitemeffect_set.all()

	# 购买价格
	@CacheHelper.staticCache
	def buyPrice(self):
		try: return self.gameitemprice
		except GameItemPrice.DoesNotExist: return None
