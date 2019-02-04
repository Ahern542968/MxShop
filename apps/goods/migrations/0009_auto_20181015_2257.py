# Generated by Django 2.0 on 2018-10-15 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_auto_20181015_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategory',
            name='category_type',
            field=models.IntegerField(choices=[(3, '三级类目'), (2, '二级类目'), (1, '一级类目')], help_text='类名级别', verbose_name='类名级别'),
        ),
    ]