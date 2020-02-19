# Generated by Django 2.2.6 on 2020-02-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exermon_module', '0003_auto_20200218_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerfragpackitem',
            name='equiped',
            field=models.BooleanField(default=False, verbose_name='是否装备中'),
        ),
        migrations.AddField(
            model_name='exerpackequip',
            name='equiped',
            field=models.BooleanField(default=False, verbose_name='是否装备中'),
        ),
        migrations.AddField(
            model_name='exerpackitem',
            name='equiped',
            field=models.BooleanField(default=False, verbose_name='是否装备中'),
        ),
        migrations.AddField(
            model_name='playerexergift',
            name='equiped',
            field=models.BooleanField(default=False, verbose_name='是否装备中'),
        ),
        migrations.AddField(
            model_name='playerexermon',
            name='equiped',
            field=models.BooleanField(default=False, verbose_name='是否装备中'),
        ),
    ]