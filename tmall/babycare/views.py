from django.shortcuts import get_object_or_404,render,redirect,render_to_response 
from django.http import HttpResponseRedirect,Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse 
from .models import Product
from django.core.paginator import Paginator
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def get_list(request):
    ids = request.POST.get('ids')
    # idstring = ''.join(ids)
    # Product.objects.extra(where=['id IN ('+ idstring +')']).delete() 
    Product.objects.filter(id=ids).delete()
    return HttpResponse('aaaa')
   

def find_list(request):
    uname = request.POST.get('uname')
    try:
        shops = Product.objects.filter(name=uname)
        data = {
            "shops":shops
        }
        return render(request,'miao/bc1.html',data)
    except Exception as e:
        raise Http404

def my_login(request,page=1):
    #分页，后面优化
    products = Product.objects.all()
    cur_page = int(page)
    # 查询posts表，按play_counts倒序排序
    posts = Product.objects.order_by('-addtime')
    paginator = Paginator(posts, 24)
    posts = paginator.page(cur_page)
    # 分页逻辑
    # 要显示的页码数量
    page_num = 5
    # 一半的页码数量
    half_page_num = page_num // 2
    first_page = 1
    last_page = paginator.num_pages
    # 如果处理当前页之前的页码不足2页
    if cur_page - half_page_num < 1:
        # 则显示的页码从当前页开始
        display_pages = range(cur_page, cur_page + page_num)
    # 如果处理当前页之后的页码不足2页
    elif cur_page + half_page_num > last_page:
        # 则从当前页往前数5页
        display_pages = range(cur_page - page_num, cur_page + 1)
    else:
        # 其他情况下，当前页左右各显示两页
        display_pages = range(cur_page - half_page_num, cur_page + half_page_num + 1)
    display_pages = list(display_pages)
    # 是否显示下一页
    if posts.has_next():
        next_page = posts.next_page_number()
    # 是否显示上一页
    if posts.has_previous():
        previous_page = posts.previous_page_number()
    # 如果当前页码范围内不包含第一页，则把第一页添加进去
    if first_page not in display_pages:
        display_pages.insert(0, first_page)
    # 如果当前页码范围内不包含最后一页，则把最后页添加进去
    if last_page not in display_pages:
        display_pages.append(last_page)
    # 把所有的局部变量传给模板
    if request.method == "GET":
        return render(request,"miao/login.html")
    elif request.method == "POST":
        uusername = request.POST.get('uname')
        upassword = request.POST.get('upassword')
        print(uusername,upassword)
        obj = User.objects.get(username=uusername)
        user = authenticate(username = uusername,password = upassword)
        if user:
            if obj.is_superuser == 1:
                return HttpResponseRedirect('/show_list/1/')
            else:
                return render(request,'miao/bc_copy.html',locals())
        else:
            render_to_response('miao/login.html')
    else:
        return HttpResponse('')

@login_required
def showlist(request, page=1):
    products = Product.objects.all()
    cur_page = int(page)
    # 查询posts表，按play_counts倒序排序
    posts = Product.objects.order_by('-addtime')
    paginator = Paginator(posts, 24)
    posts = paginator.page(cur_page)
    # 分页逻辑
    # 要显示的页码数量
    page_num = 5
    # 一半的页码数量
    half_page_num = page_num // 2
    first_page = 1
    last_page = paginator.num_pages
    # 如果处理当前页之前的页码不足2页
    if cur_page - half_page_num < 1:
        # 则显示的页码从当前页开始
        display_pages = range(cur_page, cur_page + page_num)
    # 如果处理当前页之后的页码不足2页
    elif cur_page + half_page_num > last_page:
        # 则从当前页往前数5页
        display_pages = range(cur_page - page_num, cur_page + 1)
    else:
        # 其他情况下，当前页左右各显示两页
        display_pages = range(cur_page - half_page_num, cur_page + half_page_num + 1)
    display_pages = list(display_pages)
    # 是否显示下一页
    if posts.has_next():
        next_page = posts.next_page_number()
    # 是否显示上一页
    if posts.has_previous():
        previous_page = posts.previous_page_number()
    # 如果当前页码范围内不包含第一页，则把第一页添加进去
    if first_page not in display_pages:
        display_pages.insert(0, first_page)
    # 如果当前页码范围内不包含最后一页，则把最后页添加进去
    if last_page not in display_pages:
        display_pages.append(last_page)
    # '把所有的局部变量传给模板
    return render(request,r'miao/bc.html', locals())


