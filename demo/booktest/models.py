from django.db import models

# Create your models here.


class BookInfo(models.Model):
    """图书模型对象
    b_title: 图书名称
    b_pub_date: 出版日期
    """
    b_title = models.CharField(max_length=20)
    b_pub_date = models.DateField()