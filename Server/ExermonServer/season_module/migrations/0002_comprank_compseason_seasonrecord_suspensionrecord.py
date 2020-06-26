# Generated by Django 2.2.6 on 2020-02-24 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game_module', '0002_auto_20200224_2304'),
        ('player_module', '0002_auto_20200224_2304'),
        ('season_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=64, verbose_name='描述')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('configure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.GameConfigure', verbose_name='所属配置')),
            ],
            options={
                'verbose_name': '赛季信息',
                'verbose_name_plural': '赛季信息',
            },
        ),
        migrations.CreateModel(
            name='SeasonRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.PositiveSmallIntegerField(default=0, verbose_name='赛季积分')),
                ('star_num', models.PositiveSmallIntegerField(default=0, verbose_name='段位星星')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_module.Player', verbose_name='玩家')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='season_module.CompSeason', verbose_name='赛季')),
            ],
            options={
                'verbose_name': '赛季记录',
                'verbose_name_plural': '赛季记录',
            },
        ),
        migrations.CreateModel(
            name='SuspensionRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('season_rec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='season_module.SeasonRecord', verbose_name='赛季记录')),
            ],
            options={
                'verbose_name': '禁赛记录',
                'verbose_name_plural': '禁赛记录',
            },
        ),
        migrations.CreateModel(
            name='CompRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=64, verbose_name='描述')),
                ('color', models.CharField(default='#000000', max_length=7, verbose_name='颜色')),
                ('sub_rank_num', models.PositiveSmallIntegerField(default=3, verbose_name='小段位数')),
                ('score_factor', models.PositiveSmallIntegerField(default=80, verbose_name='积分因子')),
                ('offset_factor', models.PositiveSmallIntegerField(default=60, verbose_name='抵消使用积分')),
                ('configure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.GameConfigure', verbose_name='所属配置')),
            ],
            options={
                'verbose_name': '段位信息',
                'verbose_name_plural': '段位信息',
            },
        ),
    ]
