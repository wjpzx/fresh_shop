xadmin的使用

1、安装：   pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2

2、注册进INSTALLED_APPS

```python
INSTALLED_APPS = [
		...
		'xadmin',
    	'crispy_forms',
    	'reversion',
		...
]
```

3、xadmin需要自己的数据库模型类。完成数据库迁移

```python
python manage.py makemigrations
python manage.py migrate
```

4、设置路由：替换掉原有的admin

``` python
主urls.py
import xadmin
urlpatterns = [
    ...
    path('xadmin/',xadmin.site.urls),
    ...
]
```

5、创建超级用户即刻登录

```
python manage.py createsuperuser
```

