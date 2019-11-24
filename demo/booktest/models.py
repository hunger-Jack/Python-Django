from django.db import models

# Create your models here.


class BookInfoManager(models.Manager):
    """自定义添加图书管理器对象"""
    def create_book(self, b_title, b_pub_date):
        book = self.model()  # self.model可以获取当前调用模型类对象
        book.b_title = b_title
        book.b_pub_date = b_pub_date
        book.save()
        return book


class BookInfo(models.Model):
    """图书模型对象（一类）
    b_title: 图书名称
    b_pub_date: 出版日期
    b_read: 阅读量
    b_comment: 评论量
    isDelete: 逻辑删除
    """
    b_title = models.CharField(max_length=20)
    b_pub_date = models.DateField()
    b_read = models.IntegerField(default=0)
    b_comment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    books = BookInfoManager()

    def __str__(self):
        """修改模型对象默认返回名称"""
        return self.b_title


class HeroInfo(models.Model):
    """英雄模型对象（多类）
    h_name: 英雄姓名
    h_gender: 英雄性别
    h_comment: 英雄简介
    h_book: 英雄所属图书外键
    isDelete: 逻辑删除
    """
    h_name = models.CharField(max_length=20)
    h_gender = models.BooleanField(default=True)  # 默认是True：男性，False：女性
    h_comment = models.CharField(max_length=128)
    h_book = models.ForeignKey("BookInfo", on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        """修改模型对象默认返回名称"""
        return self.h_name


class AreaInfo(models.Model):
    """地区模型对象（自关联）"""
    a_title = models.CharField("区域名称", max_length=20)
    a_parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    # 自定义字段名字
    def area_test(self):
        return self.a_title

    def parent(self):
        if not self.a_parent:
            return ""
        return self.a_parent.a_title

    # 下拉列表中输出的是对象的名称
    def __str__(self):
        return self.a_title

    # 自定义字段排序
    area_test.admin_order_field = "a_title"
    # 自定义字段重命名
    area_test.short_description = "区域名称"
    parent.short_description = "父级区域"
    parent.admin_order_field = "a_parent"
