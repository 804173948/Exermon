# Generated by Django 2.2.6 on 2020-05-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_module', '0005_auto_20200430_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quessugarprice',
            name='bound_ticket',
            field=models.PositiveIntegerField(default=0, verbose_name='绑定点券'),
        ),
    ]
