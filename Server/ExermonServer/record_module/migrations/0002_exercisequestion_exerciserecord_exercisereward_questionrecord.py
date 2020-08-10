# Generated by Django 2.2.6 on 2020-02-24 23:04

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game_module', '0002_auto_20200224_2304'),
        ('season_module', '0002_comprank_compseason_seasonrecord_suspensionrecord'),
        ('question_module', '0002_auto_20200224_2304'),
        ('player_module', '0002_auto_20200224_2304'),
        ('record_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='开始时间')),
                ('exp_incr', models.SmallIntegerField(null=True, verbose_name='经验增加')),
                ('gold_incr', models.SmallIntegerField(null=True, verbose_name='金币增加')),
                ('slot_exp_incr', models.SmallIntegerField(null=True, verbose_name='槽经验增加')),
                ('finished', models.BooleanField(default=False, verbose_name='完成标志')),
                ('count', models.PositiveSmallIntegerField(default=1, verbose_name='题量')),
                ('gen_type', models.PositiveSmallIntegerField(choices=[(0, '普通模式'), (1, '已做优先'), (2, '未做优先'), (3, '错题优先'), (4, '收藏优先'), (5, '简单题优先'), (6, '中等题优先'), (7, '难题优先')], default=0, verbose_name='生成模式')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='season_module.CompSeason', verbose_name='所属赛季')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.Subject', verbose_name='科目')),
            ],
            options={
                'verbose_name': '刷题记录',
                'verbose_name_plural': '刷题记录',
            },
        ),
        migrations.CreateModel(
            name='QuestionRecord',
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
                ('source', models.PositiveSmallIntegerField(choices=[(1, '刷题'), (2, '考核'), (3, '对战'), (4, '冒险'), (0, '其他')], default=0, verbose_name='记录来源')),
                ('collected', models.BooleanField(default=False, verbose_name='收藏标志')),
                ('wrong', models.BooleanField(default=False, verbose_name='错题标志')),
                ('note', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.models.GeneralQuestion', verbose_name='题目')),
            ],
            options={
                'verbose_name': '做题记录',
                'verbose_name_plural': '做题记录',
            },
        ),
        migrations.CreateModel(
            name='ExerciseReward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record_module.question_system.question_sets.GeneralExerciseRecord', verbose_name='刷题记录')),
            ],
            options={
                'verbose_name': '刷题奖励',
                'verbose_name_plural': '刷题奖励',
            },
        ),
        migrations.CreateModel(
            name='ExerciseQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selection', jsonfield.fields.JSONField(default=[], verbose_name='选择情况')),
                ('answered', models.BooleanField(default=False, verbose_name='作答标志')),
                ('timespan', models.PositiveIntegerField(default=0, verbose_name='用时')),
                ('exp_incr', models.SmallIntegerField(null=True, verbose_name='经验增加')),
                ('slot_exp_incr', models.SmallIntegerField(null=True, verbose_name='槽经验增加')),
                ('gold_incr', models.SmallIntegerField(null=True, verbose_name='金币增加')),
                ('is_new', models.BooleanField(default=False, verbose_name='新题标志')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record_module.question_system.question_sets.GeneralExerciseRecord', verbose_name='刷题记录')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_module.models.GeneralQuestion', verbose_name='题目')),
            ],
            options={
                'verbose_name': '刷题题目关系',
                'verbose_name_plural': '刷题题目关系',
            },
        ),
    ]
