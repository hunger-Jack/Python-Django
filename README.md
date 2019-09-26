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

## 项目应用创建
```linux
1. 创建项目
django-admin startproject demo

2. 创建应用
python manage.py startapp booktest
```

## 迁移文件
```linux
1. 创建迁移文件
python manage.py makemigrations

2. 执行迁移文件
python manage.py migrate
```

## 后台管理相关文件
```linux
1. 管理界面本地化
在setting.py里面配置
LANGUAGE_CODE = 'zh-hans' #使用中国语言
TIME_ZONE = 'Asia/Shanghai' #使用中国上海时间

2. 创建管理员
python manage.py createsuperuser  # 创建管理员账号
python manage.py runserver  # 启动服务
http://127.0.0.1:8000/admin/  # 打开管理界面

3. 注册模型
在admin.py操作
admin.site.register(模型类名称)
例如：
from booktest.models import BookInfo
admin.site.register(BookInfo)

4. 自定义管理页面
在admin.py文件，自定义类，继承自admin.ModelAdmin类

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']  # 属性list_display表示要显示哪些属性

admin.site.register(BookInfo, BookInfoAdmin)  # 添加自定义类参数

```