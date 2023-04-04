from django.http import HttpResponse
from django.shortcuts import render


def course(request):

    return render(request,'app/course.html')

def base(request):
    return render(request,'app/base.html')