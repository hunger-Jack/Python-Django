from django.db import models

# Create your models here.


class BookInfo(models.Model):
    """图书模型对象（一类）
    b_title: 图书名称
    b_pub_date: 出版日期
    """
    b_title = models.CharField(max_length=20)
    b_pub_date = models.DateField()


class HeroInfo(models.Model):
    """英雄模型对象（多类）
    h_name: 英雄姓名
    h_gender: 英雄性别
    h_comment: 英雄简介
    h_book: 英雄所属图书外键
    """
    h_name = models.CharField(max_length=20)
    h_gender = models.BooleanField(default=True)  # 默认是True：男性，False：女性
    h_comment = models.CharField(max_length=128)
    h_book = models.ForeignKey("BookInfo")