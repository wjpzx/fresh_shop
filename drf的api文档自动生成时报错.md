drf的api文档自动生成时报错

```python
Internal Server Error: /docs/
Traceback (most recent call last):
  File "D:\virtual_flask\fresh_shop\lib\site-packages\django\core\handlers\exception.py", line 34, in inner
    response = get_response(request)
  File "D:\virtual_flask\fresh_shop\lib\site-packages\django\core\handlers\base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "D:\virtual_flask\fresh_shop\lib\site-packages\django\core\handlers\base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "D:\virtual_flask\fresh_shop\lib\site-packages\django\views\decorators\csrf.py", line 54, in wrapped_view
    return view_func(*args, **kwargs)
  File "D:\virtual_flask\fresh_shop\lib\site-packages\django\views\generic\base.py", line 71, in view
    return self.dispatch(request, *args, **kwargs)
  File "D:\virtual_flask\fresh_shop\lib\site-packages\rest_framework\views.py", line 509, in dispatch
    response = self.handle_exception(exc)
  File "D:\virtual_flask\fresh_shop\lib\site-packages\rest_framework\schemas\views.py", line 48, in handle_exception
    return super().handle_exception(exc)
  File "D:\virtual_flask\fresh_shop\lib\site-packages\rest_framework\views.py", line 469, in handle_exception
    self.raise_uncaught_exception(exc)
  File "D:\virtual_flask\fresh_shop\lib\site-packages\rest_framework\views.py", line 480, in raise_uncaught_exception
    raise exc
  File "D:\virtual_flask\fresh_shop\lib\site-packages\rest_framework\views.py", line 506, in dispatch
    response = handler(request, *args, **kwargs)
  File "D:\virtual_flask\fresh_shop\lib\site-packages\rest_framework\schemas\views.py", line 37, in get
    schema = self.schema_generator.get_schema(request, self.public)
  File "D:\virtual_flask\fresh_shop\lib\site-packages\rest_framework\schemas\coreapi.py", line 156, in get_schema
    links = self.get_links(None if public else request)
  File "D:\virtual_flask\fresh_shop\lib\site-packages\rest_framework\schemas\coreapi.py", line 143, in get_links
    link = view.schema.get_link(path, method, base_url=self.url)
AttributeError: 'AutoSchema' object has no attribute 'get_link'
```

![自动生成接口文档报错信息](https://img-blog.csdnimg.cn/20190801164510594.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQ1NTAxNQ==,size_16,color_FFFFFF,t_70)

原因：REST framework可以自动帮助我们生成接口文档。REST framewrok生成接口文档需要coreapi库的支持。



解决方法：

在settings.py中重新指定schema_class的配置

```python
REST_FRAMEWORK = {
 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 新版drf schema_class默认用的是rest_framework.schemas.openapi.AutoSchema

}
```

