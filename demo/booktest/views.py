from datetime import date
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo,AreaInfo
# Create your views here.


def login_check(func):
    """检测是否登录的装饰器"""
    def wrapper_func(request, *args, **kwargs):
        # 如果cookie中有isLogin的session字段，直接返回对应视图定义的url，否则返回登录页面
        if request.session.get("isLogin"):
            print("==>测试代码<==")
            return func(request, *args, **kwargs)
        else:
            return redirect("/login_form")
    return wrapper_func


def index(request):
    """index模板"""
    # # 1. 获取模板
    # template = loader.get_template("booktest/index.html")
    #
    # # 2. 定义上下文
    # context = {"title":"图书列表","list":range(15)}
    #
    # # 3. 渲染模板
    # res_html = template.render(context)
    #
    # # 4. 返回给浏览器html内容
    # return HttpResponse(res_html)
    return render(request, "booktest/index.html", {"title":"图书列表","list":range(15)})


def show_books(request):
    """显示图书信息"""
    # 1. 从model获取图书信息
    books_list = BookInfo.books.all()
    # 2. 渲染模板
    return render(request, "booktest/show_books.html", {"books": books_list})


def show_heros(request, b_id):
    """显示英雄信息"""
    # 1. 根据b_id从model获取图书信息
    book = BookInfo.books.get(id = b_id)

    # 2. 获取与图书关联的英雄信息
    heros = book.heroinfo_set.all()

    # 3. 渲染模板
    return render(request, "booktest/show_heros.html", {"book": book, "heros": heros})


def create(request):
    """新增图书"""
    # 1. 获取图书对象
    #book = BookInfo()

    # # 2. 添加数据
    # book.b_title = "流星蝴蝶剑"
    # book.b_pub_date = date(1987, 2, 12)
    #
    # # 3. 保存
    # book.save()

    # 使用自定义管理器操作数据库添加图书
    BookInfo.books.create_book("神雕侠侣", "2012-2-12")

    # 4. 重定向/index页面
    return redirect("/books")


def delete(request, b_id):
    """删除图书"""
    # 1. 根数b_id获取图书对象
    book = BookInfo.books.get(id=b_id)

    # 2. 删除对应图书
    book.delete()

    # 3. 重定向/index页面
    return redirect("/books")


def areas(request):
    """显示地区信息"""
    # 1. 获取广州地区信息
    areas = AreaInfo.objects.get(a_title="广州市")

    # 2. 获取与广州关联的父级信息
    parent = areas.a_parent  # 多查询一注意不要加括号

    # 3. 获取与广州关联的下级信息
    children = areas.areainfo_set.all()  # 一查询多注意areainfo是小写

    # 4. 返回给浏览器信息
    return render(request, "booktest/areas.html", {"areas": areas, "parent": parent, "children": children})


def login_form(request):
    """form表单登录页面"""
    # 判断是否有isLogin字段session,如果有直接跳转修改密码页面，否则跳转登录页
    if request.session.get("isLogin"):
        return redirect("/change_pwd")
    else:
        return render(request, "booktest/login_form.html")


def login_form_check(request):
    """form表单验证"""
    # 1. 获取用户名和密码
    username = request.POST.get("username")
    password = request.POST.get("password")

    # 2. 验证用户名和密码,模拟username=rambo,password=123qwe
    if username == "rambo" and password == "123qwe":
        # 设置session标记已经登录的状态,设置用户名session
        request.session["isLogin"] = True
        request.session["username"] = username
        return redirect("/change_pwd")
    else:
        return redirect("/login_form")


def login_ajax(request):
    """ajax登录页面"""

    # 读取cookie
    cookies = request.COOKIES
    name = cookies["name"]

    # 把获取的cookie值传给login_ajax模板
    return render(request, "booktest/login_ajax.html", {"name": name})


def login_ajax_check(request):
    """ajax登录验证"""
    # 1. 获取用户名和密码
    username = request.POST.get("username")
    password = request.POST.get("password")

    # 设置cookie
    response = JsonResponse({"res": 1})
    response.set_cookie("name", "rambo", max_age=7 * 24 * 3600)

    # 2. 验证用户名和密码,模拟username=rambo,password=123qwe
    if username == "rambo" and password == "123qwe":
        # return JsonResponse({"res": 1})
        return response
    else:
        return JsonResponse({"res": 0})


@login_check
def change_pwd(request):
    """修改密码页面"""
    return render(request, "booktest/change_pwd.html")


@login_check
def change_pwd_action(request):
    """提交修改密码请求"""
    # 1. 获取修改的密码
    password = request.POST.get("password")

    # 2. 获取当前用户名
    username = request.session.get("username")

    # 3. 模拟提交数据库修改成功并且返回相应的数据
    return HttpResponse("%s 修改的密码是：%s" % (username, password))