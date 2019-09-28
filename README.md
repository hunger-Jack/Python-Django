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

1.创建项目
```linux
django-admin startproject demo
```

2.创建应用
```linux
python manage.py startapp booktest
```

3.注册应用
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booktest'  # 注册booktest应用
]
```

## 迁移文件

1.创建迁移文件
```linux
python manage.py makemigrations
```
2.执行迁移文件
```linux
python manage.py migrate
```

## 后台管理相关文件

1.管理界面本地化
```linux
在setting.py里面配置
LANGUAGE_CODE = 'zh-hans' #使用中国语言
TIME_ZONE = 'Asia/Shanghai' #使用中国上海时间
```
2.创建管理员
```linux
python manage.py createsuperuser  # 创建管理员账号
python manage.py runserver  # 启动服务
http://127.0.0.1:8000/admin/  # 打开管理界面
```
3.注册模型
```linux
在admin.py操作
admin.site.register(模型类名称)
例如：
from booktest.models import BookInfo
admin.site.register(BookInfo)
```
4.自定义管理页面
```linux
在admin.py文件，自定义类，继承自admin.ModelAdmin类

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']  # 属性list_display表示要显示哪些属性

admin.site.register(BookInfo, BookInfoAdmin)  # 添加自定义类参数

```

## 视图

1.定义视图函数
```linux
在booktest/views.py,定义各种视图函数，必须有一个参数，一般叫request，
必须返回HTTPResponse对象，HTTPResponse对象的参数是返回给浏览器的内容
例如：定义index视图函数
from django.http import HttpResponse 


def index(request):
    return HttpResponse("this is index page")
```
2.配置URL
```linux
url(正则表达式, 视图函数)
一般在项目URL中配置应用urls模块，在应用urls模块中配置各种视图函数
①配置项目中的URLconf
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('booktest.urls')),
]
②配置应用中的URLconf【注意正则表达式要严格匹配^$】
urlpatterns = [
    url(r'^index$', views.index),
]
```

## 模板

一、创建模板
```linux
1. 在项目根目录创建templates文件夹
2. 在templates文件夹创建booktest应用文件夹，可能有多个应用模板。
3. 在/templates/booktest下创建index.html模板文件
4. 设置查找模板的路径:打开test1/settings.py文件，设置TEMPLATES的DIRS值
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

二、定义模板
```html
在/templates/booktest/index.html添加如下代码

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index模板文件</title>
</head>
<body>
<h1>{{title}}</h1>
{%for i in list%}
{{i}}<br>
{%endfor%}
</body>
</html>
------------------------------------
{{变量名}}
{%代码段%}
```

三、调用模板

1.找到模板
```python
template = loader.get_template('booktest/index.html')
```

2.定义上下文：给模板文件传递数据
```python
context={'title':'图书列表','list':range(15)}
```

3.渲染模板：产生标准的html内容
```python
res_html = template.render(context)
```

简单版本的调用模板
```python
# return render(request, "模板路径", 数据)
# 例如：
def index(request):
    return render(request, "booktest/index.html", {"title":"图书列表","list":range(15)})
```

## 英雄-图书小练习

1.定义视图

①show_books视图
```python
def show_books(request):
    """显示图书信息"""
    # 1. 从model获取图书信息
    books_list = BookInfo.objects.all()
    # 2. 渲染模板
    return render(request, "booktest/show_books.html", {"books": books_list})
```
②show_heros视图
```python
def show_heros(request, b_id):
    """显示英雄信息"""
    # 1. 根据b_id从model获取图书信息
    book = BookInfo.objects.get(id = b_id)

    # 2. 获取与图书关联的英雄信息
    heros = book.heroinfo_set.all()

    # 3. 渲染模板
    return render(request, "booktest/show_heros.html", {"book": book, "heros": heros})
```

2.定义URLconf
```
①/books
②/books/图书表的id，例如：/books/2
这里需要在通过url传图书表id参数，需要在配置url时使用分组，例如：r"^books/(\d+)$"
```
3.定义模板

①show_books.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>图书信息</title>
</head>
<body>
<h1>图书信息</h1>
<ul>
    {%for book in books%}
        <li>
            <a href="/books/{{book.id}}">
                {{book.b_title}}
            </a>
        </li>
    {% endfor%}
</ul>
</body>
</html>
```

②show_heros.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>{{book.b_title}}</h1>
英雄信息：
<ul>
    {% for hero in heros %}
        <li>
            {{hero.h_name}}--{{hero.h_comment}}
        </li>
    {% empty %}
        <li>没有英雄信息</li>
    {% endfor %}
</ul>
</body>
</html>
```