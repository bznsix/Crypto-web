"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render,redirect
import os,time

def hello(request):
    # return HttpResponse('hello world')
    return render(request,'test.html')

def login(request):
    if request.method == 'GET':
        return render(request, '1.html')
    else:
        text = request.POST.get('text')
        symbol = text.split('-')[0]
        timeframe = text.split('-')[1]
        os.system('/usr/bin/python3 /home/ubuntu/Crypto/rp_msb_quant/draw_pic.py' + ' --symbol ' + symbol + ' --timeframe ' + timeframe)
        return render(request, 'test.html')


urlpatterns = [
    path('login/', login),
]
