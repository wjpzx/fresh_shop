# Generated by Django 2.2.16 on 2020-11-30 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20201127_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(choices=[('WAIT_BUYER_PAY', '交易创建'), ('TRADE_CLOSED', '超时关闭'), ('TRADE_SUCCESS', '成功'), ('paying', '待支付'), ('TRADE_FINISHED', '交易结束')], default='paying', max_length=30, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_type',
            field=models.CharField(choices=[('wechat', '微信'), ('alipay', '支付宝')], default='alipay', max_length=10, verbose_name='支付类型'),
        ),
    ]
