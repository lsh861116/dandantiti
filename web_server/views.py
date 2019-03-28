from django.shortcuts import render, redirect, HttpResponse
from web_server import models
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def loginIndex(request):
    # return HttpResponse("hello world")
    return render(request, "login.html")


#name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    #return JsonResponse(name_dict)


def regiter(request):
    if request.method == 'POST':
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        User.objects.create_user(username=username, password=password)
    else:
        return render(request, "register.html")
    return HttpResponse("注册成功")


#logout
def login(request):
    if request.method == 'GET':
        return render(request, "register.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return render(request, "index_v1.html")
        else:
            return render(request, 'register.html', {'msg': "用户名/密码错误"})
