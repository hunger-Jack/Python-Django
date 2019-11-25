from django.contrib import admin
from booktest.models import BookInfo,HeroInfo,AreaInfo,PicTest

# Register your models here.
# 后台管理相关文件-可视化操作数据库的各种操作


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "b_title", "b_pub_date"]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "h_name", "h_gender", "h_comment", "h_book_id"]


class AreaStackedInline(admin.StackedInline):
    model = AreaInfo
    extra = 2
    

class AreaInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "a_title", "area_test", "parent"]
    # 列表页每页显示数据条数
    list_per_page = 10
    # 动作执行框是否在上方
    actions_on_top = True
    # 动作执行框是否在下方
    actions_on_bottom = True
    # 右侧筛选框
    list_filter = ["a_title"]
    # 搜索框
    search_fields = ["a_title"]
    # 点击ID跳转修改页面需要展示的字段
    fields = ["a_title", "a_parent"]
    inlines = [AreaStackedInline]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(AreaInfo, AreaInfoAdmin)
admin.site.register(PicTest)