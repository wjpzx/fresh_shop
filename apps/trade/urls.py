from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

app_name="trade"

# 配置购物车的url
router.register('shopcarts',views.ShoppingCartViewset,basename="shopcarts"),
# 配置订单的url
router.register("orders",views.OrderViewSet,basename="orders")

urlpatterns = [
    re_path('^',include(router.urls))
]