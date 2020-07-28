# Generated by Django 2.2.6 on 2020-06-27 02:02

from django.db import migrations, models
import utils.model_utils


class Migration(migrations.Migration):

    dependencies = [
        ('english_pro_module', '0023_auto_20200627_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plotquestion',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=utils.model_utils.PlotQuestionImageUpload(), verbose_name='剧情图标'),
        ),
    ]
