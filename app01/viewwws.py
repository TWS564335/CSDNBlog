from django.shortcuts import render,HttpResponse

# Create your views here.
from app01.models import Book

def add(request):

    # 添加记录的方式1 ：
    # book=Book(title="北京折叠",price="11.11",pub_date="2012-12-12",publish="苹果出版社")
    # book.save()

    # 添加记录的方式2：create返回记录对象
    book_obj=Book.objects.create(title="放风筝的人3",pub_date="2016-12-12",publish="苹果出版社")
    # print(book_obj.title)
    # print(book_obj.price)
    # print(book_obj.pub_date)


    return HttpResponse("添加成功")


def query(request):
    """
    queryset :  [model对象,model对象,model对象.....]
    model对象

    API接口返回值是什么
    :param request:
    :return:
    """
    # 1 all()
    # book_list=Book.objects.all()  # 返回的是一个queryset数据类型对象，类似于 [obj,obj,.....]
    # # print(book_list)
    # for obj in book_list:
    #     print(obj.title,obj.price)

    # 2   filter     返回的是一个queryset数据类型对象，[model_obj,.....]

    # ret=Book.objects.filter(price=100)
    # # print(ret)# <QuerySet [<Book: Book object (1)>]>
    # for obj in ret:
    #     print(obj.title)

    # 3  first,last,queryset支持切片操作

    # obj=Book.objects.all().first()
    # obj=Book.objects.all().last()
    # obj=Book.objects.all()[0]
    # obj=Book.objects.all()[-1]
    # obj=Book.objects.all()[1:5]
    # print(obj.title)

    # 4 get方法   返回的就是一个model对象(有且只有一个结果的是由才有意义)
    # obj=Book.objects.get(nid=1)
    # obj=Book.objects.filter(nid=1).first()
    # # print(obj.title)

    # 5 exclude 排除,等同于filter
    # ret=Book.objects.exclude(price=100)

    # 6 order_by
    # ret=Book.objects.all().order_by("price")
    # print(ret)

    # 7 ret=Book.objects.all().order_by("price").reverse()


    # 8 count
    # ret=Book.objects.all().count()
    # print(ret)

    # 9 exists
    ret=Book.objects.all().exists()
    if ret:
        print("Ok")

    # ###################################
    # 10 values
    # book_list=Book.objects.all().values("title","price")# queryset: [{"title":"北京折叠","price":100},....]
    # print(book_list)
    '''
    <QuerySet 
    [
    {'price': Decimal('100.00'), 'title': '北京折叠'}, 
    {'price': Decimal('100.00'), 'title': '放风筝的人'}, 
    {'price': Decimal('233.00'), 'title': '西游记'}, 
    {'price': Decimal('11.00'), 'title': '水浒传'}
    ]
    >
    
    
    '''
    book_list = Book.objects.all().values_list("title", "price", "pub_date")  # queryset: [{"title":"北京折叠","price":100},....]
    print(book_list)
    '''
    <QuerySet 
    [
     ('北京折叠', Decimal('100.00'), datetime.date(2012, 12, 12)), 
     ('放风筝的人', Decimal('100.00'), datetime.date(2017, 12, 12)),
     ('西游记', Decimal('233.00'), datetime.date(2018, 6, 14)), 
     ('水浒传', Decimal('11.00'), datetime.date(2018, 6, 14))
     ]
     >
    
    '''
    # distinct（去重）
    # ret=Book.objects.all().values("price").distinct()
    # print(ret)

    #################单表查询之模糊查询 __ ##############################
    # book_list=Book.objects.filter(price__gt=100)
    # book_list=Book.objects.filter(price__lt=100)
    # book_list=Book.objects.filter(price__lte=100)
    # book_list=Book.objects.filter(price__gte=100)
    book_list=Book.objects.filter(price__in=[100,200,300])

    book_list= Book.objects.filter(price__range=[100,233])
    print(book_list)
    book_list=Book.objects.filter(title__startswith="北京")
    print(book_list)
    book_list=Book.objects.filter(title__contains="传")
    print(book_list)

    return HttpResponse("查询成功")


def change(request):
    nid=3
    Book.objects.filter(nid=nid).update(price=10,title="西游记")

    return HttpResponse("修改成功")


def delbook(request,id):

    Book.objects.filter(nid=id).delete()

    return HttpResponse("删除成功")