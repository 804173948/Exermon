from enum import Enum


class WebscoketCloseCode(Enum):

	ServerClose			= 1000 # 服务器切断连接
	ClientClose			= 1001 # 客户端切断连接
	AbnormalClose		= 1006 # 非正常断开连接

	Logout				= 3000 # 用户登出
	Kickout				= 3001 # 用户踢出


class ErrorType(Enum):
	# Common
	UnknownError = -1  # 未知错误
	Success = 0  # 成功，无错误
	InvalidRequest = 1  # 非法的请求方法
	ParameterError = 2  # 参数错误
	InvalidRoute = 3  # 非法路由
	PermissionDenied = 4  # 无权操作
	NoCurVersion = 5  # 未设置当前版本
	NoCurConfigure = 6  # 当前版本无配置
	RequestUpdate = 7  # 需要更新
	ErrorVersion = 8  # 错误的游戏版本
	InvalidUserOper = 10  # 无效的用户操作
	SubjectNotExist = 20  # 科目不存在
	BaseParamNotExist = 21  # 属性不存在
	DatabaseError = 30  # 数据库错误

	# PlayerCommon
	PlayerNotExist = 100  # 玩家不存在
	PlayerExist = 101  # 玩家已存在
	IncorrectPassword = 102  # 密码错误
	UnselectedSubject = 103  # 人物未选择该科目

	# PlayerRegister/Forget
	UsernameExist = 110  # 用户名已存在
	InvalidUsername = 111  # 非法的用户名
	InvalidPassword = 112  # 非法的密码
	PhoneExist = 113  # 电话号码已存在
	InvalidPhone = 114  # 非法的电话号码
	EmailExist = 115  # 邮箱地址已存在
	InvalidEmail = 116  # 非法的邮箱地址
	IncorrectForget = 117  # 不正确的找回密码参数
	IncorrectCode = 118  # 验证码错误
	EmailSendError = 119  # 邮件发送错误

	# PlayerLogin
	IncorrectLogin = 130  # 不正确的登陆参数
	UserAbnormal = 131  # 用户状态异常
	UserFrozen = 132  # 用户被冻结

	# PlayerInfo
	NameExist = 140  # 该名字已存在
	InvalidName = 141  # 非法的昵称
	InvalidGender = 142  # 非法的性别
	InvalidGrade = 143  # 非法的年级
	InvalidBirth = 144  # 非法的出生日期
	InvalidSchool = 145  # 非法的学校名称
	InvalidCity = 146  # 非法的居住地
	InvalidContact = 147  # 非法的联系方式
	InvalidDescription = 148  # 非法的个人介绍

	# CharacterCommon
	CharacterNotExist = 150  # 形象不存在

	# ItemCommon
	ItemNotExist = 200  # 物品不存在
	ContainerNotExist = 201  # 容器不存在
	ContItemNotExist = 202  # 容器项不存在
	ContainerNotOwner = 203  # 该容器不属于当前玩家
	ContItemNotHold = 204  # 容器中不存在该容器项
	IncorrectItemType = 210  # 物品类型不正确
	IncorrectContainerType = 211  # 容器类型不正确
	IncorrectContItemType = 212  # 容器项类型不正确

	# Gain/LostItem
	CapacityInsufficient = 220  # 容器剩余容量不足
	QuantityInsufficient = 221  # 物品数量不足
	InvalidContItem = 222  # 无效容器项

	# Equip/DequipEquip
	IncorrectEquipType = 230  # 装备类型不正确
	InvalidContainer = 231  # 无效容器

	# UseItem
	UnusableItem = 240  # 物品不可用
	InvalidItemUsing = 241  # 无效的物品使用
	ItemFrozen = 242  # 物品冻结中

	# ExermonCommon
	ExermonNotExist = 300  # 艾瑟萌不存在
	ExerGiftNotExist = 301  # 艾瑟萌天赋不存在
	ExerSlotNotExist = 302  # 艾瑟萌槽不存在
	ExerSlotItemNotExist = 303  # 艾瑟萌槽项不存在
	PlayerExermonNotExist = 304  # 玩家艾瑟萌不存在
	PlayerExerGiftNotExist = 305  # 玩家艾瑟萌天赋不存在

	# Create/Edit
	InvalidExermonCount = 310  # 非法的艾瑟萌数量
	InvalidExermonName = 311  # 非法的艾瑟萌昵称
	InvalidExermonSubject = 312  # 非法的艾瑟萌科目
	InvalidExermonType = 313  # 非法的艾瑟萌类型
	InvalidExerGiftType = 314  # 非法的艾瑟萌天赋类型

	# ExerSlot
	IncorrectSubject = 320  # 科目不正确

	# ExerEquipSlot
	InsufficientLevel = 330  # 等级不足

	# UseExerSkill
	PassiveSkill = 340  # 被动技能
	MPInsufficient = 341  # 精力值不足
	NoUseCount = 342  # 无剩余使用次数

	# QuestionCommon
	QuestionNotExist = 400  # 题目不存在
	QuesSugarNotExist = 401  # 题目糖不存在
	QuestionLinkNotExist = 402  # 题目关系不存在

	# QuestionGenerate
	InvalidGenerateConfigure = 410  # 非法的题目生成配置

	# RecordCommon
	QuestionRecordNotExist = 500  # 题目记录不存在
	ExerciseRecordNotExist = 501  # 刷题记录不存在
	ExerciseQuestionNotExist = 502  # 刷题题目不存在

	# QuestionRecord
	InvalidNote = 510  # 无效的备注格式

	# QuestionSetRecord
	QuestionNotStarted = 520  # 本题还没开始作答
	InvalidTimeSpan = 521  # 作答时间有误

	# QuestionGenerate
	GenerateError = 530  # 题目生成有误

	# QuesReport
	FeedbackTooLong = 540  # 题目反馈太长
	InvalidFeedbackType = 541  # 题目反馈类型不对
	QuesReportNotExist = 542  # 查找不到反馈记录

	# BattleCommon
	BattleNotExist = 600  # 对战不存在
	BattleRecordNotExist = 601  # 对战记录不存在
	NotInBattle = 602  # 未加入对战
	AlreadlyInBattle = 603  # 已加入对战
	BattleStarted = 604  # 对战已开始
	BattleTerminated = 605  # 对战已结束

	# BattleMatching
	IsBanned = 610  # 账号被禁赛
	AlreadyMatched = 611  # 已经匹配到对手

	# BattlePreparing
	ItemNotEquiped = 620  # 物品未装备
	IncorrectTarget = 621  # 不正确的使用目标

	# BattleQuesting
	OpponentAnswered = 630  # 对方已抢答

	# BattleActing

	# BattleResulting

	# SeasonRecord
	SeasonNotExist = 700  # 赛季不存在


class GameException(Exception):

	ERROR_DICT = {
		# Common
		ErrorType.UnknownError: "服务器发生错误，请联系管理员！",
		ErrorType.Success: "",
		ErrorType.InvalidRequest: "非法的请求方法！",
		ErrorType.ParameterError: "参数错误！",
		ErrorType.InvalidRoute: "非法的请求路由！",
		ErrorType.PermissionDenied: "无权操作！",
		ErrorType.NoCurVersion: "未设置当前版本，请联系管理员！",
		ErrorType.NoCurConfigure: "当前版本无游戏配置，请联系管理员！",
		ErrorType.RequestUpdate: "当前客户端版本过旧，请更新游戏！",
		ErrorType.ErrorVersion: "错误的客户端版本，请更新游戏！",
		ErrorType.InvalidUserOper: "无效的用户操作！",
		ErrorType.SubjectNotExist: "科目不存在！",
		ErrorType.BaseParamNotExist: "属性不存在！",
		ErrorType.DatabaseError: "数据库错误！",

		# PlayerCommon
		ErrorType.PlayerNotExist: "玩家不存在！",
		ErrorType.PlayerExist: "玩家已存在！",
		ErrorType.IncorrectPassword: "密码错误！",
		ErrorType.UnselectedSubject: "人物未选择该科目！",

		# PlayerRegister/Forget
		ErrorType.UsernameExist: "用户名已存在！",
		ErrorType.InvalidUsername: "非法的用户名格式！",
		ErrorType.InvalidPassword: "非法的密码格式！",
		ErrorType.PhoneExist: "电话号码已存在！",
		ErrorType.InvalidPhone: "非法的电话号码格式！",
		ErrorType.EmailExist: "邮箱地址已存在！",
		ErrorType.InvalidEmail: "非法的邮箱地址格式！",
		ErrorType.IncorrectForget: "用户名不存在或邮箱错误！",
		ErrorType.IncorrectCode: "验证码过时或不正确！",
		ErrorType.EmailSendError: "邮件发送错误！",

		# PlayerLogin
		ErrorType.IncorrectLogin: "用户名不存在或密码错误！",
		ErrorType.UserAbnormal: "用户状态异常，请联系管理员！",
		ErrorType.UserFrozen: "用户已被冻结，请联系管理员！",

		# PlayerInfo
		ErrorType.NameExist: "该名字已存在！",
		ErrorType.InvalidName: "非法的昵称格式！",
		ErrorType.InvalidGender: "非法的性别！",
		ErrorType.InvalidGrade: "非法的年级！",
		ErrorType.InvalidBirth: "非法的出生日期！",
		ErrorType.InvalidSchool: "非法的学校名称！",
		ErrorType.InvalidCity: "非法的居住地！",
		ErrorType.InvalidContact: "非法的联系方式！",
		ErrorType.InvalidDescription: "非法的个人介绍！",

		# CharacterCommon
		ErrorType.CharacterNotExist: "形象不存在！",

		# ItemCommon
		ErrorType.ItemNotExist: "物品不存在！",
		ErrorType.ContainerNotExist: "容器不存在！",
		ErrorType.ContItemNotExist: "物品不存在！",
		ErrorType.ContainerNotOwner: "该容器不属于当前玩家！",
		ErrorType.ContItemNotHold: "玩家未获得此物品！",
		ErrorType.IncorrectItemType: "物品类型不正确！",
		ErrorType.IncorrectContainerType: "容器类型不正确！",
		ErrorType.IncorrectContItemType: "物品类型不正确！",

		# Gain/LostItem
		ErrorType.CapacityInsufficient: "容器剩余容量不足！",
		ErrorType.QuantityInsufficient: "物品数量不足或未拥有此物品！",
		ErrorType.InvalidContItem: "无法对此物品进行操作！",

		# Equip/DequipEquip
		ErrorType.IncorrectEquipType: "装备类型不正确！",
		ErrorType.InvalidContainer: "找不到所属容器，无法进行装备操作！",

		# UseItem
		ErrorType.UnusableItem: "物品不可用！",
		ErrorType.InvalidItemUsing: "无效的物品使用！",
		ErrorType.ItemFrozen: "物品冻结中！",

		# ExermonCommon
		ErrorType.ExermonNotExist: "艾瑟萌不存在！",
		ErrorType.ExerGiftNotExist: "艾瑟萌天赋不存在！",
		ErrorType.ExerSlotNotExist: "艾瑟萌槽未创建！",
		ErrorType.ExerSlotItemNotExist: "尚未拥有该艾瑟萌槽！",
		ErrorType.PlayerExermonNotExist: "尚未拥有该艾瑟萌！",
		ErrorType.PlayerExerGiftNotExist: "尚未拥有该天赋！",

		# Create/Edit
		ErrorType.InvalidExermonCount: "非法的艾瑟萌数量！",
		ErrorType.InvalidExermonName: "非法的艾瑟萌昵称格式！",
		ErrorType.InvalidExermonSubject: "非法的艾瑟萌科目！",
		ErrorType.InvalidExermonType: "非法的艾瑟萌类型！",
		ErrorType.InvalidExerGiftType: "非法的艾瑟萌天赋类型！",

		# ExerSlot
		ErrorType.IncorrectSubject: "艾瑟萌科目与槽科目不一致！",

		# ExerEquipSlot
		ErrorType.InsufficientLevel: "艾瑟萌等级不足！",

		# UseExerSkill
		ErrorType.PassiveSkill: "被动技能无法使用！",
		ErrorType.MPInsufficient: "精力值不足！",
		ErrorType.NoUseCount: "无剩余使用次数！",

		# QuestionCommon
		ErrorType.QuestionNotExist: "题目不存在！",
		ErrorType.QuesSugarNotExist: "题目糖不存在！",
		ErrorType.QuestionLinkNotExist: "题目不存在！",

		# QuestionGenerate
		ErrorType.InvalidGenerateConfigure: "非法的题目生成配置！",

		# RecordCommon
		ErrorType.QuestionRecordNotExist: "题目记录不存在！",
		ErrorType.ExerciseRecordNotExist: "刷题记录不存在！",
		ErrorType.ExerciseQuestionNotExist: "刷题题目不存在！",

		# QuestionRecord
		ErrorType.InvalidNote: "无效的备注格式",

		# QuestionSetRecord
		ErrorType.QuestionNotStarted: "本题还没开始作答！",
		ErrorType.InvalidTimeSpan: "作答时间有误！",

		# QuestionGenerate
		ErrorType.GenerateError: "题目生成有误！",

		# QuesReport
		ErrorType.QuesReportTooLong: "题目反馈太长！",
		ErrorType.InvalidQuesReportType: "题目反馈类型不对！",
		ErrorType.QuesReportNotExist: "查找不到反馈记录！",
    
		# BattleCommon
		ErrorType.BattleNotExist: "对战不存在！",
		ErrorType.BattleRecordNotExist: "对战记录不存在！",
		ErrorType.NotInBattle: "尚未加入对战！",
		ErrorType.AlreadlyInBattle: "已加入一场对战！",
		ErrorType.BattleStarted: "对战已开始！",
		ErrorType.BattleTerminated: "对战已结束！",

		# BattleMatching
		ErrorType.IsBanned: "您因信誉积分不足，暂时已被禁赛！如有疑问请联系管理员。",
		ErrorType.AlreadyMatched: "已经匹配到对手！",

		# BattlePreparing
		ErrorType.ItemNotEquiped: "所使用的物品未被装备！",
		ErrorType.IncorrectTarget: "不正确的使用目标！",

		# BattleQuesting
		ErrorType.OpponentAnswered: "对方已抢答！",

		# BattleActing

		# BattleResulting
    
		# SeasonRecord
		ErrorType.SeasonNotExist: "赛季不存在！",
	}

	def __init__(self, error_type: ErrorType):
		"""

		Args:
			error_type (ErrorType): 错误类型
		"""
		self.error_type = error_type
		self.msg = GameException.ERROR_DICT[error_type]

	def __str__(self):
		return self.msg
