"""fresh_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework.routers import DefaultRouter
import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from django.views.static import serve
from django.urls import path, include, re_path

from fresh_shop.settings import MEDIA_ROOT,STATICFILES_DIRS

router = DefaultRouter()
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    # 文件
    re_path('^static/(?P<path>.*)$', serve, {'document_root': STATICFILES_DIRS}, name='static'),
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    # drf文档，title可自定义
    path('docs/',include_docs_urls(title='生鲜超市')),
    path('api-auth/',include('rest_framework.urls')),
    # token
    path('api-token-auth/',views.obtain_auth_token),
    # jwt的token认证接口
    path('jwt-auth/',obtain_jwt_token),
    # jwt的认证接口
    path('login/',obtain_jwt_token),

    path('goods/',include('goods.urls',namespace="goods")),
    path('user/',include('user.urls',namespace="user")),
    path('user_ope/',include('user_operation.urls',namespace="user_ope")),
    path('trade/',include('trade.urls',namespace="trade")),
    re_path('^',include(router.urls))
]
