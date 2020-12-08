from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import GoodsSerializer,CategorySerializer
from .models import Goods,GoodsCategory
from .filters import GoodsFilter


# Create your views here.


# class GoodsListView(APIView):
#     """
#     商品列表展示
#     """
#     def get(self,request,format=None):
#         goods = Goods.objects.all()
#         goods_serializer = GoodsSerializer(goods,many=True)
#         return Response(goods_serializer.data,status=status.HTTP_200_OK)


# class GoodsListView(ListModelMixin,GenericAPIView):
#     """
#     商品列表页
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# 自定义分页功能
class GoodsPagination(PageNumberPagination):
    """
    商品列表自定义分页
    """
    # 默认每页显示的个数
    page_size = 12
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页面参数
    page_query_param = 'page'
    # 每页最大显示条数
    max_page_size = 100


# class GoodsListView(ListAPIView):
#     """商品列表页"""
#     pagination_class = GoodsPagination   # 分页
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer


class GoodsListViewSet(ListModelMixin,RetrieveModelMixin,GenericViewSet):
    """
    商品列表页
    """
    # 分页
    pagination_class = GoodsPagination
    # 这里必须要在模型类的Meta里定义一个默认的排序，否则会报错(不影响正常使用)
    queryset = Goods.objects.all()

    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)

    # 设置filter的类为我们自定义的类
    filter_class = GoodsFilter
    # 搜索，=name表示精确搜索，也可以使用各种正则表达式
    search_fields = ('name', 'goods_brief', 'goods_desc')
    # 排序
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(ListModelMixin,RetrieveModelMixin,GenericViewSet):
    """
    list：
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
