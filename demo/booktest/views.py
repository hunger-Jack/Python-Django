from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
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