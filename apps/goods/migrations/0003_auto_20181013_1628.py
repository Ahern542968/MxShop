# Generated by Django 2.0 on 2018-10-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20180829_0005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.RemoveField(
            model_name='goodsimage',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='image',
            field=models.ImageField(max_length=200, upload_to='brands/'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='图片'),
        ),
    ]
