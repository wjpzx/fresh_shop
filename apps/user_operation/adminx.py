import xadmin
from . import models

# Register your models here.


class UserFavAdmin(object):
    list_display = ['user', 'goods', 'add_time']


class UserLeavingMessageAdmin(object):
    list_display = ['user','message_type', 'message', 'add_time']


class UserAddressAdmin(object):
    list_display = ['signer_name', 'signer_mobile', 'district' , 'address']


xadmin.site.register(models.UserFav,UserFavAdmin)
xadmin.site.register(models.UserAddress,UserAddressAdmin)
xadmin.site.register(models.UserLeaVingMessage,UserLeavingMessageAdmin)