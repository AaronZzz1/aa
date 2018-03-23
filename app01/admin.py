from django.contrib import admin

# Register your models here.


from app01.models import Area,PicInfo


class AreaAdmin(admin.ModelAdmin):
    ...
    # 定义列表中要显示哪些字段(也可以指定方法名)
    list_display = ['id','title','parent_id']

admin.site.register(Area,AreaAdmin)

admin.site.register(PicInfo)