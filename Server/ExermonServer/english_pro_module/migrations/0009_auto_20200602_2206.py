# Generated by Django 2.2.6 on 2020-06-02 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english_pro_module', '0008_merge_20200602_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exerprorecord',
            name='finished',
        ),
        migrations.RemoveField(
            model_name='infinitivequestion',
            name='infinitive_type',
        ),
        migrations.AddField(
            model_name='infinitivequestion',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, '[包含 sb. 的短语选项]'), (2, '[do 形式的短语选项]'), (3, '[介词短语选项]')], default=2, verbose_name='修改类型'),
        ),
        migrations.AlterField(
            model_name='word',
            name='chinese',
            field=models.CharField(max_length=256, verbose_name='中文'),
        ),
        migrations.AlterField(
            model_name='word',
            name='type',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='词性'),
        ),
        migrations.AlterField(
            model_name='wrongitem',
            name='word',
            field=models.TextField(blank=True, null=True, verbose_name='正确单词'),
        ),
    ]
