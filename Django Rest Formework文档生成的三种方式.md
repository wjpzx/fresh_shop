Django Rest Formework文档生成的三种方式

​	需安装  django-coreapi和pyyaml库，可通过pip install安装

1、Schema

- 在settings.py内添加

  ```python
  REST_FRAMEWORK = {
  	'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
  }
  ```

- 在urls.py中添加如下配置

  ```python
  from rest_framework.schemas import get_schema_view
  schema_view = get_schema_view(title="慕雪超市 API文档",description="所有API文档")
  path('schema/',schema_view),
  ```

2、coreapi  **推荐**

- settings.py内添加如下配置

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
  }
  ```

- 在urls.py写入路由

  ```python
  from rest_framework.documentation import include_docs_urls
  path('docs/',include_docs_urls(title="慕雪超市",description="所有API文档"))
  ```
  
  
  
- ![img](https://images2018.cnblogs.com/blog/1299879/201804/1299879-20180414221224302-2010871713.png)

  

3、openapi

- ​	只需在urls.py中写入路由

  ```python
  from rest_framework.schemas import get_schema_view
  
  path('openapi', get_schema_view(
          title="Your Project",
          description="API for all things …"
      ), name='openapi-schema'),
  ```

  

