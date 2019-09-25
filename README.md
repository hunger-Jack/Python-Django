# Python-Django

## 目录结构
```
├── booktest
|  ├── __init__.py  # 说明booktest是一个python包
|  ├── admin.py  # 网站后台管理相关文件
|  ├── apps.py  # 应用配置文件
|  ├── migrations  # 在Django应用中的model类和数据库结构的schema之间进行同步
|  |  └── __init__.py
|  ├── models.py  # 数据库相关操作
|  ├── tests.py  # 开发测试文件
|  └── views.py  # 接受浏览器请求进行处理，返回页面相关内容
├── demo
|  ├── __init__.py  # 说明demo是一个python的包
|  ├── settings.py  # 配置文件
|  ├── urls.py  # 路由配置文件
|  └── wsgi.py  # 服务器和django的交互入口
└── manage.py  # Django项目管理工具
```