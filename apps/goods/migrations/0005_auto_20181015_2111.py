# Generated by Django 2.0 on 2018-10-15 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20181014_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategory',
            name='category_type',
            field=models.IntegerField(choices=[(1, '一级类目'), (3, '三级类目'), (2, '二级类目')], help_text='类名级别', verbose_name='类名级别'),
        ),
    ]
