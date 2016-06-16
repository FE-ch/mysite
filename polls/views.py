# -*- coding: utf-8 -*-
# @Author: root
# @Date:   2016-06-16 13:20:48
# @Last Modified by:   root
# @Last Modified time: 2016-06-16 13:20:56


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
