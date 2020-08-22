# Generated by Django 2.2.6 on 2020-08-22 00:08

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import utils.model_utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player_module', '0002_auto_20200822_0008'),
        ('game_module', '0002_auto_20200822_0008'),
        ('question_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorrectingQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='收录时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '正常'), (1, '异常'), (-1, '其他')], default=0, verbose_name='状态')),
                ('score', models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='分值')),
                ('source', models.TextField(blank=True, null=True, verbose_name='来源')),
                ('description', models.TextField(blank=True, null=True, verbose_name='题解')),
                ('is_primary', models.BooleanField(default=True, verbose_name='是否小学题目')),
                ('is_middle', models.BooleanField(default=True, verbose_name='是否初中题目')),
                ('is_high', models.BooleanField(default=True, verbose_name='是否高中题目')),
                ('for_test', models.BooleanField(default=False, verbose_name='测试')),
                ('article', models.TextField(verbose_name='文章')),
                ('subject', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game_module.Subject', verbose_name='科目')),
            ],
            options={
                'verbose_name': '改错题',
                'verbose_name_plural': '改错题',
            },
        ),
        migrations.CreateModel(
            name='ListeningQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='收录时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '正常'), (1, '异常'), (-1, '其他')], default=0, verbose_name='状态')),
                ('score', models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='分值')),
                ('source', models.TextField(blank=True, null=True, verbose_name='来源')),
                ('description', models.TextField(blank=True, null=True, verbose_name='题解')),
                ('is_primary', models.BooleanField(default=True, verbose_name='是否小学题目')),
                ('is_middle', models.BooleanField(default=True, verbose_name='是否初中题目')),
                ('is_high', models.BooleanField(default=True, verbose_name='是否高中题目')),
                ('for_test', models.BooleanField(default=False, verbose_name='测试')),
                ('article', models.TextField(blank=True, null=True, verbose_name='文章')),
                ('times', models.PositiveSmallIntegerField(default=2, verbose_name='重复次数')),
                ('audio', models.FileField(upload_to=utils.model_utils.QuestionAudioUpload(), verbose_name='音频文件')),
                ('subject', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game_module.Subject', verbose_name='科目')),
            ],
            options={
                'verbose_name': '组合题',
                'verbose_name_plural': '组合题',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='收录时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '正常'), (1, '异常'), (-1, '其他')], default=0, verbose_name='状态')),
                ('score', models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='分值')),
                ('source', models.TextField(blank=True, null=True, verbose_name='来源')),
                ('description', models.TextField(blank=True, null=True, verbose_name='题解')),
                ('is_primary', models.BooleanField(default=True, verbose_name='是否小学题目')),
                ('is_middle', models.BooleanField(default=True, verbose_name='是否初中题目')),
                ('is_high', models.BooleanField(default=True, verbose_name='是否高中题目')),
                ('for_test', models.BooleanField(default=False, verbose_name='测试')),
                ('word', models.CharField(max_length=64, verbose_name='单词')),
                ('chinese', models.CharField(max_length=64, verbose_name='中文')),
                ('phrase', models.CharField(max_length=64, verbose_name='不定式项')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, '包含 sb. 的短语选项'), (2, 'do 形式的短语选项'), (3, '介词短语选项')], default=2, verbose_name='修改类型')),
                ('subject', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game_module.Subject', verbose_name='科目')),
            ],
            options={
                'verbose_name': '元素',
                'verbose_name_plural': '元素',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReadingQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='收录时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '正常'), (1, '异常'), (-1, '其他')], default=0, verbose_name='状态')),
                ('score', models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='分值')),
                ('source', models.TextField(blank=True, null=True, verbose_name='来源')),
                ('description', models.TextField(blank=True, null=True, verbose_name='题解')),
                ('is_primary', models.BooleanField(default=True, verbose_name='是否小学题目')),
                ('is_middle', models.BooleanField(default=True, verbose_name='是否初中题目')),
                ('is_high', models.BooleanField(default=True, verbose_name='是否高中题目')),
                ('for_test', models.BooleanField(default=False, verbose_name='测试')),
                ('article', models.TextField(blank=True, null=True, verbose_name='文章')),
                ('subject', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game_module.Subject', verbose_name='科目')),
            ],
            options={
                'verbose_name': '组合题',
                'verbose_name_plural': '组合题',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='收录时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '正常'), (1, '异常'), (-1, '其他')], default=0, verbose_name='状态')),
                ('score', models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='分值')),
                ('source', models.TextField(blank=True, null=True, verbose_name='来源')),
                ('description', models.TextField(blank=True, null=True, verbose_name='题解')),
                ('is_primary', models.BooleanField(default=True, verbose_name='是否小学题目')),
                ('is_middle', models.BooleanField(default=True, verbose_name='是否初中题目')),
                ('is_high', models.BooleanField(default=True, verbose_name='是否高中题目')),
                ('for_test', models.BooleanField(default=False, verbose_name='测试')),
                ('english', models.CharField(max_length=64, verbose_name='英文')),
                ('chinese', models.CharField(max_length=256, verbose_name='中文')),
                ('type', models.CharField(blank=True, max_length=64, null=True, verbose_name='词性')),
                ('level', models.PositiveSmallIntegerField(default=1, verbose_name='等级')),
                ('subject', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game_module.Subject', verbose_name='科目')),
            ],
            options={
                'verbose_name': '元素',
                'verbose_name_plural': '元素',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WrongItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence_index', models.PositiveSmallIntegerField(verbose_name='句子编号')),
                ('word_index', models.PositiveSmallIntegerField(verbose_name='单词编号')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, '增加'), (2, '修改'), (3, '删除')], default=2, verbose_name='修改类型')),
                ('word', models.TextField(blank=True, null=True, verbose_name='正确单词')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.CorrectingQuestion', verbose_name='改错题目')),
            ],
            options={
                'verbose_name': '改错题错误项',
                'verbose_name_plural': '改错题错误项',
            },
        ),
        migrations.CreateModel(
            name='WordReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, '题目错误'), (2, '图片错误'), (3, '答案错误'), (4, '解析错误'), (5, '科目错误'), (6, '难度分配错误'), (7, '多个错误'), (0, '其他错误')], verbose_name='类型')),
                ('description', models.CharField(max_length=256, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='反馈时间')),
                ('result', models.CharField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('result_time', models.DateTimeField(blank=True, null=True, verbose_name='处理时间')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.Word', verbose_name='题目')),
            ],
            options={
                'verbose_name': '题目反馈',
                'verbose_name_plural': '题目反馈',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WordRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='次数')),
                ('correct', models.PositiveSmallIntegerField(default=0, verbose_name='正确数')),
                ('last_date', models.DateTimeField(null=True, verbose_name='上次做题日期')),
                ('first_date', models.DateTimeField(null=True, verbose_name='初次做题日期')),
                ('first_time', models.PositiveIntegerField(default=0, verbose_name='初次用时')),
                ('avg_time', models.PositiveIntegerField(default=0, verbose_name='平均用时')),
                ('corr_time', models.PositiveIntegerField(null=True, verbose_name='首次正确用时')),
                ('sum_exp', models.PositiveSmallIntegerField(default=0, verbose_name='上次得分')),
                ('sum_gold', models.PositiveSmallIntegerField(default=0, verbose_name='平均得分')),
                ('source', models.PositiveSmallIntegerField(choices=[(1, '刷题'), (2, '考核'), (3, '对战'), (4, '冒险'), (5, '特训'), (0, '其他')], default=0, verbose_name='记录来源')),
                ('collected', models.BooleanField(default=False, verbose_name='收藏标志')),
                ('wrong', models.BooleanField(default=False, verbose_name='错题标志')),
                ('note', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
                ('current', models.BooleanField(default=False, verbose_name='是否是当前轮')),
                ('current_correct', models.BooleanField(default=None, null=True, verbose_name='当前轮是否答对')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.Word', verbose_name='题目')),
            ],
            options={
                'verbose_name': '做题记录',
                'verbose_name_plural': '做题记录',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReadingSubQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='收录时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '正常'), (1, '异常'), (-1, '其他')], default=0, verbose_name='状态')),
                ('score', models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='分值')),
                ('source', models.TextField(blank=True, null=True, verbose_name='来源')),
                ('description', models.TextField(blank=True, null=True, verbose_name='题解')),
                ('is_primary', models.BooleanField(default=True, verbose_name='是否小学题目')),
                ('is_middle', models.BooleanField(default=True, verbose_name='是否初中题目')),
                ('is_high', models.BooleanField(default=True, verbose_name='是否高中题目')),
                ('for_test', models.BooleanField(default=False, verbose_name='测试')),
                ('title', models.TextField(verbose_name='题干')),
                ('sel_type', models.PositiveSmallIntegerField(choices=[(0, '单选题'), (1, '多选题'), (2, '判断题')], default=0, verbose_name='类型')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.ReadingQuestion', verbose_name='题目')),
                ('subject', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game_module.Subject', verbose_name='科目')),
            ],
            options={
                'verbose_name': '选择题',
                'verbose_name_plural': '选择题',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReadingQuesReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, '题目错误'), (2, '图片错误'), (3, '答案错误'), (4, '解析错误'), (5, '科目错误'), (6, '难度分配错误'), (7, '多个错误'), (0, '其他错误')], verbose_name='类型')),
                ('description', models.CharField(max_length=256, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='反馈时间')),
                ('result', models.CharField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('result_time', models.DateTimeField(blank=True, null=True, verbose_name='处理时间')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.ReadingQuestion', verbose_name='题目')),
            ],
            options={
                'verbose_name': '题目反馈',
                'verbose_name_plural': '题目反馈',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReadingQuesRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='次数')),
                ('correct', models.PositiveSmallIntegerField(default=0, verbose_name='正确数')),
                ('last_date', models.DateTimeField(null=True, verbose_name='上次做题日期')),
                ('first_date', models.DateTimeField(null=True, verbose_name='初次做题日期')),
                ('first_time', models.PositiveIntegerField(default=0, verbose_name='初次用时')),
                ('avg_time', models.PositiveIntegerField(default=0, verbose_name='平均用时')),
                ('corr_time', models.PositiveIntegerField(null=True, verbose_name='首次正确用时')),
                ('sum_exp', models.PositiveSmallIntegerField(default=0, verbose_name='上次得分')),
                ('sum_gold', models.PositiveSmallIntegerField(default=0, verbose_name='平均得分')),
                ('source', models.PositiveSmallIntegerField(choices=[(1, '刷题'), (2, '考核'), (3, '对战'), (4, '冒险'), (5, '特训'), (0, '其他')], default=0, verbose_name='记录来源')),
                ('collected', models.BooleanField(default=False, verbose_name='收藏标志')),
                ('wrong', models.BooleanField(default=False, verbose_name='错题标志')),
                ('note', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.ReadingQuestion', verbose_name='题目')),
            ],
            options={
                'verbose_name': '做题记录',
                'verbose_name_plural': '做题记录',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReadingQuesChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(verbose_name='编号')),
                ('text', models.TextField(verbose_name='文本')),
                ('answer', models.BooleanField(default=False, verbose_name='正误')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.ReadingSubQuestion', verbose_name='题目')),
            ],
            options={
                'verbose_name': '题目选项',
                'verbose_name_plural': '题目选项',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlotQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='收录时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '正常'), (1, '异常'), (-1, '其他')], default=0, verbose_name='状态')),
                ('score', models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='分值')),
                ('source', models.TextField(blank=True, null=True, verbose_name='来源')),
                ('description', models.TextField(blank=True, null=True, verbose_name='题解')),
                ('is_primary', models.BooleanField(default=True, verbose_name='是否小学题目')),
                ('is_middle', models.BooleanField(default=True, verbose_name='是否初中题目')),
                ('is_high', models.BooleanField(default=True, verbose_name='是否高中题目')),
                ('for_test', models.BooleanField(default=False, verbose_name='测试')),
                ('title', models.TextField(verbose_name='题干')),
                ('sel_type', models.PositiveSmallIntegerField(choices=[(0, '单选题'), (1, '多选题'), (2, '判断题')], default=0, verbose_name='类型')),
                ('plot', models.TextField(verbose_name='剧情内容')),
                ('picture', models.ImageField(blank=True, null=True, upload_to=utils.model_utils.PlotQuestionImageUpload(), verbose_name='剧情图标')),
                ('subject', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game_module.Subject', verbose_name='科目')),
            ],
            options={
                'verbose_name': '选择题',
                'verbose_name_plural': '选择题',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlotQuesChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(verbose_name='编号')),
                ('text', models.TextField(verbose_name='文本')),
                ('answer', models.BooleanField(default=False, verbose_name='正误')),
                ('gold', models.PositiveSmallIntegerField(default=0, verbose_name='所需金币')),
                ('result_text', models.TextField(verbose_name='选项对应的结果文本')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.PlotQuestion', verbose_name='题目')),
            ],
            options={
                'verbose_name': '题目选项',
                'verbose_name_plural': '题目选项',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlotChoiceEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveSmallIntegerField(choices=[(0, '空'), (10, '回复体力值'), (11, '回复精力值'), (20, '增加能力值'), (21, '临时增加能力值'), (22, '战斗中增加能力值'), (30, '获得物品'), (31, '获得金币'), (32, '获得绑定点券'), (40, '指定艾瑟萌获得经验'), (41, '指定艾瑟萌槽项获得经验'), (42, '玩家获得经验'), (99, '执行程序')], default=0, verbose_name='效果编号')),
                ('params', jsonfield.fields.JSONField(default=[], verbose_name='效果参数')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.PlotQuesChoice', verbose_name='选项')),
            ],
            options={
                'verbose_name': '剧情题目效果',
                'verbose_name_plural': '剧情题目效果',
            },
        ),
        migrations.CreateModel(
            name='PhraseReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, '题目错误'), (2, '图片错误'), (3, '答案错误'), (4, '解析错误'), (5, '科目错误'), (6, '难度分配错误'), (7, '多个错误'), (0, '其他错误')], verbose_name='类型')),
                ('description', models.CharField(max_length=256, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='反馈时间')),
                ('result', models.CharField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('result_time', models.DateTimeField(blank=True, null=True, verbose_name='处理时间')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.Phrase', verbose_name='题目')),
            ],
            options={
                'verbose_name': '题目反馈',
                'verbose_name_plural': '题目反馈',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhraseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='次数')),
                ('correct', models.PositiveSmallIntegerField(default=0, verbose_name='正确数')),
                ('last_date', models.DateTimeField(null=True, verbose_name='上次做题日期')),
                ('first_date', models.DateTimeField(null=True, verbose_name='初次做题日期')),
                ('first_time', models.PositiveIntegerField(default=0, verbose_name='初次用时')),
                ('avg_time', models.PositiveIntegerField(default=0, verbose_name='平均用时')),
                ('corr_time', models.PositiveIntegerField(null=True, verbose_name='首次正确用时')),
                ('sum_exp', models.PositiveSmallIntegerField(default=0, verbose_name='上次得分')),
                ('sum_gold', models.PositiveSmallIntegerField(default=0, verbose_name='平均得分')),
                ('source', models.PositiveSmallIntegerField(choices=[(1, '刷题'), (2, '考核'), (3, '对战'), (4, '冒险'), (5, '特训'), (0, '其他')], default=0, verbose_name='记录来源')),
                ('collected', models.BooleanField(default=False, verbose_name='收藏标志')),
                ('wrong', models.BooleanField(default=False, verbose_name='错题标志')),
                ('note', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.Phrase', verbose_name='题目')),
            ],
            options={
                'verbose_name': '做题记录',
                'verbose_name_plural': '做题记录',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ListeningSubQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='收录时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '正常'), (1, '异常'), (-1, '其他')], default=0, verbose_name='状态')),
                ('score', models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='分值')),
                ('source', models.TextField(blank=True, null=True, verbose_name='来源')),
                ('description', models.TextField(blank=True, null=True, verbose_name='题解')),
                ('is_primary', models.BooleanField(default=True, verbose_name='是否小学题目')),
                ('is_middle', models.BooleanField(default=True, verbose_name='是否初中题目')),
                ('is_high', models.BooleanField(default=True, verbose_name='是否高中题目')),
                ('for_test', models.BooleanField(default=False, verbose_name='测试')),
                ('title', models.TextField(verbose_name='题干')),
                ('sel_type', models.PositiveSmallIntegerField(choices=[(0, '单选题'), (1, '多选题'), (2, '判断题')], default=0, verbose_name='类型')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.ListeningQuestion', verbose_name='题目')),
                ('subject', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game_module.Subject', verbose_name='科目')),
            ],
            options={
                'verbose_name': '选择题',
                'verbose_name_plural': '选择题',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ListeningQuesReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, '题目错误'), (2, '图片错误'), (3, '答案错误'), (4, '解析错误'), (5, '科目错误'), (6, '难度分配错误'), (7, '多个错误'), (0, '其他错误')], verbose_name='类型')),
                ('description', models.CharField(max_length=256, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='反馈时间')),
                ('result', models.CharField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('result_time', models.DateTimeField(blank=True, null=True, verbose_name='处理时间')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.ListeningQuestion', verbose_name='题目')),
            ],
            options={
                'verbose_name': '题目反馈',
                'verbose_name_plural': '题目反馈',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ListeningQuesRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='次数')),
                ('correct', models.PositiveSmallIntegerField(default=0, verbose_name='正确数')),
                ('last_date', models.DateTimeField(null=True, verbose_name='上次做题日期')),
                ('first_date', models.DateTimeField(null=True, verbose_name='初次做题日期')),
                ('first_time', models.PositiveIntegerField(default=0, verbose_name='初次用时')),
                ('avg_time', models.PositiveIntegerField(default=0, verbose_name='平均用时')),
                ('corr_time', models.PositiveIntegerField(null=True, verbose_name='首次正确用时')),
                ('sum_exp', models.PositiveSmallIntegerField(default=0, verbose_name='上次得分')),
                ('sum_gold', models.PositiveSmallIntegerField(default=0, verbose_name='平均得分')),
                ('source', models.PositiveSmallIntegerField(choices=[(1, '刷题'), (2, '考核'), (3, '对战'), (4, '冒险'), (5, '特训'), (0, '其他')], default=0, verbose_name='记录来源')),
                ('collected', models.BooleanField(default=False, verbose_name='收藏标志')),
                ('wrong', models.BooleanField(default=False, verbose_name='错题标志')),
                ('note', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.ListeningQuestion', verbose_name='题目')),
            ],
            options={
                'verbose_name': '做题记录',
                'verbose_name_plural': '做题记录',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ListeningQuesChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(verbose_name='编号')),
                ('text', models.TextField(verbose_name='文本')),
                ('answer', models.BooleanField(default=False, verbose_name='正误')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.ListeningSubQuestion', verbose_name='题目')),
            ],
            options={
                'verbose_name': '题目选项',
                'verbose_name_plural': '题目选项',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='收录时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '正常'), (1, '异常'), (-1, '其他')], default=0, verbose_name='状态')),
                ('score', models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='分值')),
                ('source', models.TextField(blank=True, null=True, verbose_name='来源')),
                ('description', models.TextField(blank=True, null=True, verbose_name='题解')),
                ('is_primary', models.BooleanField(default=True, verbose_name='是否小学题目')),
                ('is_middle', models.BooleanField(default=True, verbose_name='是否初中题目')),
                ('is_high', models.BooleanField(default=True, verbose_name='是否高中题目')),
                ('for_test', models.BooleanField(default=False, verbose_name='测试')),
                ('title', models.TextField(verbose_name='题干')),
                ('sel_type', models.PositiveSmallIntegerField(choices=[(0, '单选题'), (1, '多选题'), (2, '判断题')], default=0, verbose_name='类型')),
                ('level', models.SmallIntegerField(default=0, verbose_name='附加等级')),
                ('star', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game_module.QuestionStar', verbose_name='星级')),
                ('subject', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game_module.Subject', verbose_name='科目')),
            ],
            options={
                'verbose_name': '选择题',
                'verbose_name_plural': '选择题',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralQuesReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, '题目错误'), (2, '图片错误'), (3, '答案错误'), (4, '解析错误'), (5, '科目错误'), (6, '难度分配错误'), (7, '多个错误'), (0, '其他错误')], verbose_name='类型')),
                ('description', models.CharField(max_length=256, verbose_name='描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='反馈时间')),
                ('result', models.CharField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('result_time', models.DateTimeField(blank=True, null=True, verbose_name='处理时间')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.GeneralQuestion', verbose_name='题目')),
            ],
            options={
                'verbose_name': '题目反馈',
                'verbose_name_plural': '题目反馈',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralQuesRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='次数')),
                ('correct', models.PositiveSmallIntegerField(default=0, verbose_name='正确数')),
                ('last_date', models.DateTimeField(null=True, verbose_name='上次做题日期')),
                ('first_date', models.DateTimeField(null=True, verbose_name='初次做题日期')),
                ('first_time', models.PositiveIntegerField(default=0, verbose_name='初次用时')),
                ('avg_time', models.PositiveIntegerField(default=0, verbose_name='平均用时')),
                ('corr_time', models.PositiveIntegerField(null=True, verbose_name='首次正确用时')),
                ('sum_exp', models.PositiveSmallIntegerField(default=0, verbose_name='上次得分')),
                ('sum_gold', models.PositiveSmallIntegerField(default=0, verbose_name='平均得分')),
                ('source', models.PositiveSmallIntegerField(choices=[(1, '刷题'), (2, '考核'), (3, '对战'), (4, '冒险'), (5, '特训'), (0, '其他')], default=0, verbose_name='记录来源')),
                ('collected', models.BooleanField(default=False, verbose_name='收藏标志')),
                ('wrong', models.BooleanField(default=False, verbose_name='错题标志')),
                ('note', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.GeneralQuestion', verbose_name='题目')),
            ],
            options={
                'verbose_name': '做题记录',
                'verbose_name_plural': '做题记录',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralQuesPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='序号')),
                ('desc_pic', models.BooleanField(default=False, verbose_name='解析图片')),
                ('file', models.ImageField(upload_to=utils.model_utils.QuestionImageUpload(), verbose_name='图片文件')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.GeneralQuestion', verbose_name='题目')),
            ],
            options={
                'verbose_name': '题目图片',
                'verbose_name_plural': '题目图片',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralQuesChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(verbose_name='编号')),
                ('text', models.TextField(verbose_name='文本')),
                ('answer', models.BooleanField(default=False, verbose_name='正误')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.GeneralQuestion', verbose_name='题目')),
            ],
            options={
                'verbose_name': '题目选项',
                'verbose_name_plural': '题目选项',
                'abstract': False,
            },
        ),
    ]