# Generated by Django 2.2.16 on 2020-11-30 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'ordering': ['-market_price'], 'verbose_name': '商品信息', 'verbose_name_plural': '商品信息'},
        ),
    ]