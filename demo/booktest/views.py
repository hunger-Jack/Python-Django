from datetime import date
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo
# Create your views here.


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
    books_list = BookInfo.objects.all()
    # 2. 渲染模板
    return render(request, "booktest/show_books.html", {"books": books_list})


def show_heros(request, b_id):
    """显示英雄信息"""
    # 1. 根据b_id从model获取图书信息
    book = BookInfo.objects.get(id = b_id)

    # 2. 获取与图书关联的英雄信息
    heros = book.heroinfo_set.all()

    # 3. 渲染模板
    return render(request, "booktest/show_heros.html", {"book": book, "heros": heros})


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