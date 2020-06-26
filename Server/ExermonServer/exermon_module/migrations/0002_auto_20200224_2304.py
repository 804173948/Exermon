# Generated by Django 2.2.6 on 2020-02-24 23:04

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import utils.model_utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game_module', '0002_auto_20200224_2304'),
        ('player_module', '0002_auto_20200224_2304'),
        ('exermon_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerEquip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=128, verbose_name='描述')),
                ('sell_price', models.PositiveIntegerField(default=0, verbose_name='出售价格')),
                ('discardable', models.BooleanField(default=True, verbose_name='可丢弃')),
                ('tradable', models.BooleanField(default=True, verbose_name='可交易')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=utils.model_utils.ItemIconUpload(), verbose_name='图标')),
                ('e_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.ExerEquipType', verbose_name='装备类型')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.ItemStar', verbose_name='星级')),
            ],
            options={
                'verbose_name': '艾瑟萌装备',
                'verbose_name_plural': '艾瑟萌装备',
            },
        ),
        migrations.CreateModel(
            name='ExerEquipPriceInline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gold', models.PositiveIntegerField(default=0, verbose_name='金币')),
                ('ticket', models.PositiveIntegerField(default=0, verbose_name='点券')),
                ('bound_ticket', models.PositiveIntegerField(default=0, verbose_name='金币')),
            ],
            options={
                'verbose_name': '货币',
                'verbose_name_plural': '货币',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExerEquipSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '艾瑟萌装备槽',
                'verbose_name_plural': '艾瑟萌装备槽',
            },
        ),
        migrations.CreateModel(
            name='ExerFrag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=128, verbose_name='描述')),
                ('count', models.PositiveSmallIntegerField(default=16, verbose_name='所需碎片数')),
                ('sell_price', models.PositiveIntegerField(default=0, verbose_name='出售价格')),
            ],
            options={
                'verbose_name': '艾瑟萌碎片',
                'verbose_name_plural': '艾瑟萌碎片',
            },
        ),
        migrations.CreateModel(
            name='ExerFragPack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.PositiveSmallIntegerField(default=0, verbose_name='容量')),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
            ],
            options={
                'verbose_name': '艾瑟萌碎片背包',
                'verbose_name_plural': '艾瑟萌碎片背包',
            },
        ),
        migrations.CreateModel(
            name='ExerGift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=128, verbose_name='描述')),
                ('color', models.CharField(default='#FFFFFF', max_length=7, verbose_name='标志颜色')),
                ('g_type', models.PositiveSmallIntegerField(choices=[(1, '初始天赋'), (2, '其他天赋')], default=1, verbose_name='艾瑟萌天赋类型')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.ExerGiftStar', verbose_name='艾瑟萌星级')),
            ],
            options={
                'verbose_name': '艾瑟萌天赋',
                'verbose_name_plural': '艾瑟萌天赋',
            },
        ),
        migrations.CreateModel(
            name='ExerGiftPool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.PositiveSmallIntegerField(default=0, verbose_name='容量')),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
            ],
            options={
                'verbose_name': '艾瑟萌天赋池',
                'verbose_name_plural': '艾瑟萌天赋池',
            },
        ),
        migrations.CreateModel(
            name='ExerHub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.PositiveSmallIntegerField(default=0, verbose_name='容量')),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
            ],
            options={
                'verbose_name': '艾瑟萌仓库',
                'verbose_name_plural': '艾瑟萌仓库',
            },
        ),
        migrations.CreateModel(
            name='ExerItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=128, verbose_name='描述')),
                ('sell_price', models.PositiveIntegerField(default=0, verbose_name='出售价格')),
                ('discardable', models.BooleanField(default=True, verbose_name='可丢弃')),
                ('tradable', models.BooleanField(default=True, verbose_name='可交易')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=utils.model_utils.ItemIconUpload(), verbose_name='图标')),
                ('max_count', models.PositiveSmallIntegerField(default=99, verbose_name='叠加数量')),
                ('battle_use', models.BooleanField(default=True, verbose_name='对战道具')),
                ('menu_use', models.BooleanField(default=True, verbose_name='背包道具')),
                ('adventure_use', models.BooleanField(default=True, verbose_name='冒险道具')),
                ('consumable', models.BooleanField(default=False, verbose_name='消耗品')),
                ('freeze', models.PositiveSmallIntegerField(default=0, verbose_name='冻结回合')),
                ('rate', models.PositiveSmallIntegerField(default=0, verbose_name='使用几率')),
                ('i_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.UsableItemType', verbose_name='物品类型')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.ItemStar', verbose_name='星级')),
            ],
            options={
                'verbose_name': '艾瑟萌物品',
                'verbose_name_plural': '艾瑟萌物品',
            },
        ),
        migrations.CreateModel(
            name='ExerItemPriceInline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gold', models.PositiveIntegerField(default=0, verbose_name='金币')),
                ('ticket', models.PositiveIntegerField(default=0, verbose_name='点券')),
                ('bound_ticket', models.PositiveIntegerField(default=0, verbose_name='金币')),
            ],
            options={
                'verbose_name': '货币',
                'verbose_name_plural': '货币',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exermon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=128, verbose_name='描述')),
                ('animal', models.CharField(max_length=24, verbose_name='品种')),
                ('full', models.ImageField(blank=True, null=True, upload_to=utils.model_utils.ExermonImageUpload('full'), verbose_name='全身像')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=utils.model_utils.ExermonImageUpload('icon'), verbose_name='缩略图')),
                ('battle', models.ImageField(blank=True, null=True, upload_to=utils.model_utils.ExermonImageUpload('battle'), verbose_name='战斗图')),
                ('e_type', models.PositiveSmallIntegerField(choices=[(1, '初始艾瑟萌'), (2, '野生艾瑟萌'), (3, '剧情艾瑟萌'), (4, '稀有艾瑟萌')], default=1, verbose_name='艾瑟萌类型')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.ExerStar', verbose_name='艾瑟萌星级')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.Subject', verbose_name='科目')),
            ],
            options={
                'verbose_name': '艾瑟萌',
                'verbose_name_plural': '艾瑟萌',
            },
        ),
        migrations.CreateModel(
            name='ExerPack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.PositiveSmallIntegerField(default=0, verbose_name='容量')),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
            ],
            options={
                'verbose_name': '艾瑟萌背包',
                'verbose_name_plural': '艾瑟萌背包',
            },
        ),
        migrations.CreateModel(
            name='ExerSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=128, verbose_name='描述')),
                ('passive', models.BooleanField(default=False, verbose_name='被动技能')),
                ('need_count', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='次数需求')),
                ('mp_cost', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='MP消耗')),
                ('rate', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='使用几率')),
                ('freeze', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='冻结时间')),
                ('max_use_count', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='最大使用次数')),
                ('target_type', models.PositiveSmallIntegerField(blank=True, choices=[(0, '无'), (1, '己方'), (2, '敌方'), (3, '双方随机'), (4, '双方全部')], default=2, null=True, verbose_name='目标')),
                ('hit_type', models.PositiveSmallIntegerField(blank=True, choices=[(0, '无'), (1, '体力值伤害'), (2, '体力值回复'), (3, '体力值吸收'), (4, '精力值伤害'), (5, '精力值回复'), (6, '精力值吸收')], default=1, null=True, verbose_name='命中类型')),
                ('atk_rate', models.PositiveSmallIntegerField(blank=True, default=100, null=True, verbose_name='攻击比率')),
                ('def_rate', models.PositiveSmallIntegerField(blank=True, default=100, null=True, verbose_name='防御比率')),
                ('plus_formula', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='附加公式')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=utils.model_utils.SkillImageUpload('icon'), verbose_name='图标')),
                ('ani', models.ImageField(blank=True, null=True, upload_to=utils.model_utils.SkillImageUpload('ani'), verbose_name='技能动画')),
                ('target_ani', models.ImageField(blank=True, null=True, upload_to=utils.model_utils.SkillImageUpload('target'), verbose_name='击中动画')),
                ('next_skill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerSkill', verbose_name='下级技能')),
                ('o_exermon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exermon_module.Exermon', verbose_name='艾瑟萌')),
            ],
            options={
                'verbose_name': '艾瑟萌技能',
                'verbose_name_plural': '艾瑟萌技能',
            },
        ),
        migrations.CreateModel(
            name='ExerSkillSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '艾瑟萌技能槽',
                'verbose_name_plural': '艾瑟萌技能槽',
            },
        ),
        migrations.CreateModel(
            name='ExerSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
            ],
            options={
                'verbose_name': '艾瑟萌槽',
                'verbose_name_plural': '艾瑟萌槽',
            },
        ),
        migrations.CreateModel(
            name='PlayerExermon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='叠加数量')),
                ('equiped', models.BooleanField(default=False, verbose_name='是否装备中')),
                ('nickname', models.CharField(blank=True, max_length=4, null=True, verbose_name='艾瑟萌昵称')),
                ('exp', models.PositiveIntegerField(default=0, verbose_name='经验值')),
                ('level', models.PositiveSmallIntegerField(default=1, verbose_name='等级')),
                ('container', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerHub', verbose_name='容器')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exermon_module.Exermon', verbose_name='物品')),
            ],
            options={
                'verbose_name': '玩家艾瑟萌',
                'verbose_name_plural': '玩家艾瑟萌',
            },
        ),
        migrations.CreateModel(
            name='PlayerExerGift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='叠加数量')),
                ('equiped', models.BooleanField(default=False, verbose_name='是否装备中')),
                ('container', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerGiftPool', verbose_name='容器')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerGift', verbose_name='物品')),
            ],
            options={
                'verbose_name': '玩家艾瑟萌天赋',
                'verbose_name_plural': '玩家艾瑟萌天赋',
            },
        ),
        migrations.CreateModel(
            name='GiftParamRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0, verbose_name='属性值')),
                ('gift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerGift', verbose_name='艾瑟萌天赋')),
                ('param', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.BaseParam', verbose_name='属性类型')),
            ],
            options={
                'verbose_name': '艾瑟萌天赋成长加成率',
                'verbose_name_plural': '艾瑟萌天赋成长加成率',
            },
        ),
        migrations.CreateModel(
            name='ExerSlotItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='槽编号')),
                ('exp', models.PositiveIntegerField(default=0, verbose_name='经验值')),
                ('container', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerSlot', verbose_name='容器')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
                ('player_exer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exermon_module.PlayerExermon', verbose_name='装备艾瑟萌')),
                ('player_gift', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exermon_module.PlayerExerGift', verbose_name='装备天赋')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.Subject', verbose_name='科目')),
            ],
            options={
                'verbose_name': '艾瑟萌槽项',
                'verbose_name_plural': '艾瑟萌槽项',
            },
        ),
        migrations.CreateModel(
            name='ExerSkillSlotItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='槽编号')),
                ('use_count', models.PositiveIntegerField(default=0, verbose_name='使用次数')),
                ('container', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerSkillSlot', verbose_name='容器')),
                ('skill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerSkill', verbose_name='技能')),
            ],
            options={
                'verbose_name': '艾瑟萌技能槽项',
                'verbose_name_plural': '艾瑟萌技能槽项',
            },
        ),
        migrations.AddField(
            model_name='exerskillslot',
            name='player_exer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exermon_module.PlayerExermon', verbose_name='艾瑟萌'),
        ),
        migrations.CreateModel(
            name='ExerSkillEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveSmallIntegerField(choices=[(0, '空'), (10, '回复体力值'), (11, '回复精力值'), (20, '增加能力值'), (21, '临时增加能力值'), (22, '战斗中增加能力值'), (30, '获得物品'), (31, '获得金币'), (32, '获得绑定点券'), (40, '指定艾瑟萌获得经验'), (41, '指定艾瑟萌槽项获得经验'), (42, '玩家获得经验'), (99, '执行程序')], default=0, verbose_name='效果编号')),
                ('params', jsonfield.fields.JSONField(default=[], verbose_name='效果参数')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerSkill', verbose_name='物品')),
            ],
            options={
                'verbose_name': '技能使用效果',
                'verbose_name_plural': '技能使用效果',
            },
        ),
        migrations.CreateModel(
            name='ExerParamRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0, verbose_name='属性值')),
                ('exermon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exermon_module.Exermon', verbose_name='艾瑟萌')),
                ('param', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.BaseParam', verbose_name='属性类型')),
            ],
            options={
                'verbose_name': '艾瑟萌属性成长率',
                'verbose_name_plural': '艾瑟萌属性成长率',
            },
        ),
        migrations.CreateModel(
            name='ExerParamBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0, verbose_name='属性值')),
                ('exermon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exermon_module.Exermon', verbose_name='艾瑟萌')),
                ('param', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.BaseParam', verbose_name='属性类型')),
            ],
            options={
                'verbose_name': '艾瑟萌基础属性值',
                'verbose_name_plural': '艾瑟萌基础属性值',
            },
        ),
        migrations.CreateModel(
            name='ExerPackItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='叠加数量')),
                ('equiped', models.BooleanField(default=False, verbose_name='是否装备中')),
                ('container', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerPack', verbose_name='容器')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerItem', verbose_name='物品')),
            ],
            options={
                'verbose_name': '艾瑟萌背包物品',
                'verbose_name_plural': '艾瑟萌背包物品',
            },
        ),
        migrations.CreateModel(
            name='ExerPackEquip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='叠加数量')),
                ('equiped', models.BooleanField(default=False, verbose_name='是否装备中')),
                ('container', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerPack', verbose_name='容器')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerEquip', verbose_name='物品')),
            ],
            options={
                'verbose_name': '艾瑟萌背包装备',
                'verbose_name_plural': '艾瑟萌背包装备',
            },
        ),
        migrations.CreateModel(
            name='ExerItemPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gold', models.PositiveIntegerField(default=0, verbose_name='金币')),
                ('ticket', models.PositiveIntegerField(default=0, verbose_name='点券')),
                ('bound_ticket', models.PositiveIntegerField(default=0, verbose_name='金币')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerItem', verbose_name='物品')),
            ],
            options={
                'verbose_name': '艾瑟萌物品价格',
                'verbose_name_plural': '艾瑟萌物品价格',
            },
        ),
        migrations.CreateModel(
            name='ExerItemEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveSmallIntegerField(choices=[(0, '空'), (10, '回复体力值'), (11, '回复精力值'), (20, '增加能力值'), (21, '临时增加能力值'), (22, '战斗中增加能力值'), (30, '获得物品'), (31, '获得金币'), (32, '获得绑定点券'), (40, '指定艾瑟萌获得经验'), (41, '指定艾瑟萌槽项获得经验'), (42, '玩家获得经验'), (99, '执行程序')], default=0, verbose_name='效果编号')),
                ('params', jsonfield.fields.JSONField(default=[], verbose_name='效果参数')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerItem', verbose_name='物品')),
            ],
            options={
                'verbose_name': '艾瑟萌物品使用效果',
                'verbose_name_plural': '艾瑟萌物品使用效果',
            },
        ),
        migrations.CreateModel(
            name='ExerFragPackItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='叠加数量')),
                ('equiped', models.BooleanField(default=False, verbose_name='是否装备中')),
                ('container', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerFragPack', verbose_name='容器')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerFrag', verbose_name='物品')),
            ],
            options={
                'verbose_name': '艾瑟萌碎片背包物品',
                'verbose_name_plural': '艾瑟萌碎片背包物品',
            },
        ),
        migrations.AddField(
            model_name='exerfrag',
            name='o_exermon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exermon_module.Exermon', verbose_name='所属艾瑟萌'),
        ),
        migrations.CreateModel(
            name='ExerEquipSlotItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='槽编号')),
                ('container', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerEquipSlot', verbose_name='容器')),
                ('e_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.ExerEquipType', verbose_name='装备槽类型')),
                ('pack_equip', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exermon_module.ExerPackEquip', verbose_name='装备')),
            ],
            options={
                'verbose_name': '艾瑟萌装备槽项',
                'verbose_name_plural': '艾瑟萌装备槽项',
            },
        ),
        migrations.AddField(
            model_name='exerequipslot',
            name='exer_slot',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerSlotItem', verbose_name='艾瑟萌'),
        ),
        migrations.CreateModel(
            name='ExerEquipPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gold', models.PositiveIntegerField(default=0, verbose_name='金币')),
                ('ticket', models.PositiveIntegerField(default=0, verbose_name='点券')),
                ('bound_ticket', models.PositiveIntegerField(default=0, verbose_name='金币')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerEquip', verbose_name='物品')),
            ],
            options={
                'verbose_name': '艾瑟萌装备价格',
                'verbose_name_plural': '艾瑟萌装备价格',
            },
        ),
        migrations.CreateModel(
            name='ExerEquipParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0, verbose_name='属性值')),
                ('equip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerEquip', verbose_name='装备')),
                ('param', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.BaseParam', verbose_name='属性类型')),
            ],
            options={
                'verbose_name': '艾瑟萌装备属性值',
                'verbose_name_plural': '艾瑟萌装备属性值',
            },
        ),
    ]
