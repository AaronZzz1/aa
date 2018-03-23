from django.db import models

# Create your models here.

class Area(models.Model):
    """地区类"""
    title = models.CharField(max_length=50)
    # 外键： 自关联
    parent = models.ForeignKey('self', null=True, blank=True)

#定义图片类

class PicInfo(models.Model):

    # 上传图片保存的路径(注意：相对于上面MEDIA_ROOT指定的static / media目录)
    pic_path = models.ImageField(upload_to='app01')