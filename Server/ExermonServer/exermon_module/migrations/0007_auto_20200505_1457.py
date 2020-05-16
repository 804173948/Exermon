# Generated by Django 2.2.6 on 2020-05-05 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_module', '0003_auto_20200226_1009'),
        ('exermon_module', '0006_auto_20200421_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exerequipparam',
            options={'verbose_name': '艾瑟萌装备基础属性值', 'verbose_name_plural': '艾瑟萌装备基础属性值'},
        ),
        migrations.RemoveField(
            model_name='exerequip',
            name='param_rate',
        ),
        migrations.RemoveField(
            model_name='exerequip',
            name='param_type',
        ),
        migrations.CreateModel(
            name='ExerEquipLevelParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0, verbose_name='属性值')),
                ('equip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exermon_module.ExerEquip', verbose_name='装备')),
                ('param', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_module.BaseParam', verbose_name='属性类型')),
            ],
            options={
                'verbose_name': '艾瑟萌装备等级属性值',
                'verbose_name_plural': '艾瑟萌装备等级属性值',
            },
        ),
    ]