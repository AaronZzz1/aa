import os

from django.core.paginator import Paginator
from django.http import HttpResponse,JsonResponse
# from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from app01.models import PicInfo, Area
from project04_其他 import settings


def index(request):

    print('===inde视图函数===')

    # print("aa"+None)


    return render(request, 'app01/index.html')

#自定义上传图片
def upload(request):

    return render(request,'app01/upload.html')

def do_upload(request):

    #获取对象
    pic_file = request.FILES.get('pic')
    print("xixi:%s" % pic_file)

    #定义路径
    file_path = "%s/app01/%s" % (settings.MEDIA_ROOT,pic_file.name)
    print("哈哈哈%s" % file_path)

    with open(file_path,'wb') as file:
        for data in pic_file.chunks():
            file.write(data)

    pic_info = PicInfo()
    pic_info.pic_path = 'app01/%s' % pic_file.name
    pic_info.save()

    #响应浏览器
    return HttpResponse('上传成功！')


def show_images(request):
    pics = PicInfo.objects.all()
    #pics是一个Que.set对象，要取到下标才能.(点)出来！！！
    data = {'pics':pics}
    return render(request,'app01/show_image.html',data)


def shwo_areas(request):

    # area = Area.objects.filter(parent_id = 1)
    # my_list = []
    # for pro in area:
    #     my_list.append((pro.id,pro.title))
    #
    # datas= {'area':my_list}
    #



    return render(request,'app01/show_areas.html')

def get_provinces(request):
    area = Area.objects.filter(parent_id=1)
    my_list = []
    for pro in area:
        my_list.append((pro.id, pro.title))

    datas = {'area': my_list}

    return JsonResponse(datas)

#只要设置一个可以显示下级的视图函数就行了
def get_children(request, parent_id):
    parent = Area.objects.get(id = parent_id)
    chlidren = parent.area_set.all()

    area_arr = []
    for city in chlidren:
        area_arr.append((city.id,city.title))
    json = {'children':area_arr}
    return JsonResponse(json)



def show_page(request,page_on=1):
    provinces = Area.objects.filter(parent_id=1)
    # 创建分页对象(每页显示10条)
    paginator = Paginator(provinces,10)

    #通过Paginator对象来获取当前页
    page = paginator.page(page_on) #第一页


    datas = {'page':page}

    return render(request,'app01/show_page.html',datas)