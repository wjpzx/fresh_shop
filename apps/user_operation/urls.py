from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from .views import UserFavViewset, LeavingMessageViewset, AddressViewset

app_name = "user_ope"

router = DefaultRouter()
# 配置用户收藏的url
router.register('userfavs', UserFavViewset, basename="userfavs")
# 配置用户留言的url
router.register('messages',LeavingMessageViewset,basename="messages")
# 配置收货地址
router.register('address',AddressViewset,basename="address")

urlpatterns = [
    re_path('^',include(router.urls))
]