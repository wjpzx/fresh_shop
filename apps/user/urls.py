from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from .views import SmsCodeViewset,UserViewset

app_name = "user"

router = DefaultRouter()
# 配置codes的url
router.register('codes',SmsCodeViewset,basename="code")
router.register('users',UserViewset,basename="users")

urlpatterns = [
    re_path('^',include(router.urls))
]