from django.contrib import admin
from booktest.models import BookInfo,HeroInfo

# Register your models here.
# 后台管理相关文件-可视化操作数据库的各种操作


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "b_title", "b_pub_date"]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "h_name", "h_gender", "h_comment", "h_book_id"]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)