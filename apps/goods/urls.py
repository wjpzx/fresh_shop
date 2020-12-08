from rest_framework.routers import DefaultRouter

from django.urls import path,re_path,include

from .view_base import GoodsListView
from . import views

app_name = 'goods'

router = DefaultRouter()
# 配置goods的url
router.register('goods',views.GoodsListViewSet)
router.register('categorys',views.CategoryViewSet,basename="categorys")

urlpatterns = [
    # path('good/',GoodsListView.as_view(),name='good'),
    # path('list/',views.GoodsListView.as_view(),name='list'),

    re_path('^',include(router.urls))
]