from django.shortcuts import render
from .models import Article, Reporter, Person
from django.http import HttpResponse
from django.http import Http404
import datetime

# Create your views here.


def article(request):
    a_list = Article.objects.all()
    str_out=''
    for i in a_list:
        str_out+=i.headline+' '
    return HttpResponse(str_out)

def reporter(request, id):
    a_list = Reporter.objects.all()
    str_out=''
    for i in a_list:
        str_out+=i.full_name+' '+id+ ' '
    return HttpResponse(str_out)

def index(request):
    return HttpResponse("Hello, world. This is INDEX")

def person(request, id):
    persons_all = Person.objects.all()
    out_list=[]
    out_list.append('You entered ' + id )
    out_list.append('Coincides with:')
    k=1
    for item in persons_all:
        item_name = item.name.lower()
        if id.lower() in item_name.split(' '):
            k=0
            pers_age = str(age(item.born))
            out_list.append(item.name)
            out_list.append(pers_age)
            out_list.append(item.article.headline)
            out_list.append(item.article.reporter.full_name)
           # str_out += 'Name: '+pers_name+'<p> Years old: '+ pers_age +'<p> Mentioned in article: ' +\
             #         str(item.article.headline) + '<p>Written by: '+ str(item.article.reporter.full_name)+'<p>'
    if k: raise Http404("Question does not exist")
    context = {'out_list': out_list}
    return render(request, 'page/person.html', context)


def statistics(request):
    a_list = Article.objects.all()
    arts=0
    for i in a_list: arts+=1
    a_list=Reporter.objects.all()
    reps=0
    for i in a_list: reps+=1
    str_out='Reporters: '+str(arts)+' Articles: '+str(reps)
    return HttpResponse(str_out)

def age (born):
# born has datetime format, like datetime.date(2011,2,1)
    today = datetime.date.today()
    return int((today.year - born.year) + ((today.month > born.month) or
    ((today.month == born.month) and (today.day >= born.day))))

