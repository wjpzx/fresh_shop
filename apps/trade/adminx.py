import xadmin
from . import models

# Register your models here.


class ShoppingCartAdmin(object):
    list_display = ['user', 'goods', 'nums']


class OrderInfoAdmin(object):
    list_display = ['user','order_sn', 'trade_no', 'pay_status', 'post_script' , 'order_mount', 'pay_time', 'add_time']

    class OrderGodsInline(object):
        model = models.OrderGoods
        exclude = ['add_time']
        extra = 1
        style = 'tab'

    inlines = [OrderGodsInline]


xadmin.site.register(models.ShoppingCart,ShoppingCartAdmin)
xadmin.site.register(models.OrderInfo,OrderInfoAdmin)