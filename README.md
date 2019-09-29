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

## 中途把sqlite改为mysql

1.把原有数据导出
```linux
python manage.py dumpdata > data.json
```
2.修改数据库配置文件
```python
# /demo/demo/settings.py

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'books_heros',  # 数据库名字
        'USER': 'root',  # 数据库登录账号
        'PASSWORD': '123qwe',  # 数据库登录密码
        'HOST': 'localhost',  # 数据库所在主机
        'PORT': 3306  # 数据库所在端口
    }
}
```
3.安装pymysql包
```linux
pip install pymysql
```
4.使MySQLdb支持pymysql
```python
# /demo/demo/__init__.py

import pymysql
pymysql.install_as_MySQLdb()
```
5.处理报错信息-ImproperlyConfigured
```linux
  File "/Users/lanbo/.local/share/virtualenvs/py_django/lib/python3.6/site-packages/django/db/backends/mysql/base.py", line 36, in <module>
    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.
```
解决方法：根据你的提示路径打开`base.py`，把35、36 行前面加 # 注释掉就好了，就像下面这样：
```linux
 34 version = Database.version_info
 35 #if version < (1, 3, 13):
 36 #    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you     have %s.' % Database.__version__)
```
6.处理报错信息-AttributeError
```linux
  File "/Users/lanbo/.local/share/virtualenvs/py_django/lib/python3.6/site-packages/django/db/backends/mysql/operations.py", line 146, in last_executed_query
    query = query.decode(errors='replace')
AttributeError: 'str' object has no attribute 'decode'
```
解决方法：根据提示打开报错的文件 operations.py，找到 146 行，把 decode 改成 encode 即可，类似下面这样：
```linux
140     def last_executed_query(self, cursor, sql, params):
141         # With MySQLdb, cursor objects have an (undocumented) "_executed"
142         # attribute where the exact query sent to the database is saved.
143         # See MySQLdb/cursors.py in the source distribution.
144         query = getattr(cursor, '_executed', None)
145         if query is not None:
146             query = query.encode(errors='replace')	# 这里把 decode 改为 encode
147         return query
```
7.数据库迁移
```linux
python manage.py migrate
```
8.导入数据到mysql中的books_heros数据库中
```linux
python manage.py loaddata data.json
```

## 数据库添加新的字段和新的数据
1.在models添加新的字段
```python
class BookInfo(models.Model):
    """图书模型对象（一类）
    b_title: 图书名称
    b_pub_date: 出版日期
    b_read: 阅读量----新增
    b_comment: 评论量----新增
    isDelete: 逻辑删除----新增
    """
    b_title = models.CharField(max_length=20)
    b_pub_date = models.DateField()
    b_read = models.IntegerField(default=0)
    b_comment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        """修改模型对象默认返回名称"""
        return self.b_title


class HeroInfo(models.Model):
    """英雄模型对象（多类）
    h_name: 英雄姓名
    h_gender: 英雄性别
    h_comment: 英雄简介
    h_book: 英雄所属图书外键
    isDelete: 逻辑删除----新增
    """
    h_name = models.CharField(max_length=20)
    h_gender = models.BooleanField(default=True)  # 默认是True：男性，False：女性
    h_comment = models.CharField(max_length=128)
    h_book = models.ForeignKey("BookInfo", on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        """修改模型对象默认返回名称"""
        return self.h_name
```
2.创建迁移文件
```linux
python manage.py makemigrations
```
3.执行迁移文件
```linux
python manage.py migrate
```
4.在数据库插入数据
```sql
insert into booktest_bookinfo(b_title,b_pub_date,b_read,b_comment,isDelete) values 
('射雕英雄传','1980-5-1',12,34,0), ('天龙八部','1986-7-24',36,40,0), 
('笑傲江湖','1995-12-24',20,80,0), ('雪山飞狐','1987-11-11',58,24,0);

insert into booktest_heroinfo(h_name,h_gender,h_book_id,h_comment,isDelete) values 
('郭靖',1,4,'降龙十八掌',0), ('黄蓉',0,4,'打狗棍法',0), 
('黄药师',1,4,'弹指神通',0), ('欧阳锋',1,4,'蛤蟆功',0), 
('梅超风',0,4,'九阴白骨爪',0), ('乔峰',1,5,'降龙十八掌',0), 
('段誉',1,5,'六脉神剑',0), ('虚竹',1,5,'天山六阳掌',0), 
('王语嫣',0,5,'神仙姐姐',0), ('令狐冲',1,6,'独孤九剑',0), 
('任盈盈',0,6,'弹琴',0), ('岳不群',1,6,'华山剑法',0), 
('东方不败',0,6,'葵花宝典',0), ('胡斐',1,7,'胡家刀法',0), 
('苗若兰',0,7,'黄衣',0), ('程灵素',0,7,'医术',0), 
('袁紫衣',0,7,'六合拳',0);
```
## 修改视图
1.修改show_books模板，添加【新增】和【删除】按钮
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>图书信息</title>
</head>
<body>
<a href="/create">新增图书</a>
<h1>图书信息</h1>
<ul>
    {%for book in books%}
        <li>
            <a href="/books/{{book.id}}">
                {{book.b_title}}
            </a>----
            <a href="/delete{{bbook.id}}">删除</a>
        </li>
    {% endfor%}
</ul>
</body>
</html>
```
2.添加/create，/delete新增图书视图和删除图书视图
```python
def create(request):
    """新增图书"""
    # 1. 获取图书对象
    book = BookInfo()

    # 2. 添加数据
    book.b_title = "流星蝴蝶剑"
    book.b_pub_date = date(1987, 2, 12)

    # 3. 保存
    book.save()

    # 4. 重定向/index页面
    return redirect("/books")

def delete(request, b_id):
    """删除图书"""
    # 1. 根数b_id获取图书对象
    book = BookInfo.objects.get(id=b_id)

    # 2. 删除对应图书
    book.delete()

    # 3. 重定向/index页面
    return redirect("/books")
```

3.修改URLconf
```python
urlpatterns = [
    re_path(r"^index$", views.index),
    re_path(r"^books$", views.show_books),
    re_path(r"^books/(\d+)$", views.show_heros),
    re_path(r"^create$", views.create),
    re_path(r"^delete(\d+)$", views.delete)
]
```