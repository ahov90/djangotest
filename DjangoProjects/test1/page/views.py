from django.shortcuts import render

# Create your views here.
from .models import Article, Reporter
from django.http import HttpResponse

def article(request):
    a_list = Article.objects.all()
    str_out=''
    for i in a_list:
        str_out+=i.headline+' '
    return HttpResponse(str_out)

def reporter(request):
    a_list = Reporter.objects.all()
    str_out=''
    for i in a_list:
        str_out+=i.full_name+' '
    return HttpResponse(str_out)

def index(request):
    return HttpResponse("Hello, world. This is INDEX")

def statistics(request):
    a_list = Article.objects.all()
    arts=0
    for i in a_list: arts+=1
    a_list=Reporter.objects.all()
    reps=0
    for i in a_list: reps+=1
    str_out='Reporters: '+str(arts)+' Articles: '+str(reps)
    return HttpResponse(str_out)


