from django.shortcuts import render
from .models import Article, Reporter, Person
from django.core.paginator import Paginator, InvalidPage, PageNotAnInteger
import datetime

# Create your views here.

def test (request, test_id):

    test_list=[]

    all_list=[]
    all_list.append(Reporter.objects.all())
    all_list.append(Article.objects.all())
    all_list.append(Person.objects.all())

    test_list.append(test_id)
    try:
        get_par=request.GET['id']
        get_par=str(get_par)
        test_list.append(get_par)
    except: pass
    try:
        get_par=request.GET['page_num']
        get_par=str(get_par)
        test_list.append(get_par)
    except: pass

    context = {'test_list': test_list, 'all_list': all_list}
    return render(request, 'page/test.html', context)

def article(request, id_art, page_num):

    all_list=[]
    all_list.append(Reporter.objects.all())
    all_list.append(Article.objects.all())
    all_list.append(Person.objects.all())

    pers_list=[]

    try:
        art = Article.objects.get(id=id_art)
    except:
        art_list = Article.objects.all()
        context = {'out_list': art_list, 'all_list':all_list}
        return render(request, 'page/all_articles.html', context)

    pers_set = art.person_set.all()

    for item in pers_set:
        item.age = str(age(item.born))
        pers_list.append(item)

    pag = Paginator(pers_list,2)
    try:
        pagined=pag.page(page_num)
    except InvalidPage:
        pagined=pag.page(1)

    context = {'all_list':all_list, 'art': art, 'pers_list': pagined }
    return render(request, 'page/article.html', context)


def reporter(request, id_rep=0):
    all_list=[]
    all_list.append(Reporter.objects.all())
    all_list.append(Article.objects.all())
    all_list.append(Person.objects.all())
    out_list = []
    try:
        rep = Reporter.objects.get(id=id_rep)
    except:
        out_list = Reporter.objects.all()
        context = {'out_list': out_list , 'all_list':all_list}
        return render(request, 'page/all_reporters.html', context)
    out_list.append(rep)
    art_set = rep.article_set.all()
    for item in art_set:
        out_list.append(item)
    context = {'out_list': out_list, 'all_list':all_list}
    return render(request, 'page/reporter.html', context)

def index(request):
    all_list=[]
    all_list.append(Reporter.objects.all())
    all_list.append(Article.objects.all())
    all_list.append(Person.objects.all())
    context = {'all_list': all_list}
    return render(request, 'page/index.html', context)

def person(request, id_pers, page_num):
    all_list=[]
    all_list.append(Reporter.objects.all())
    all_list.append(Article.objects.all())
    all_list.append(Person.objects.all())
    try:
        pers = Person.objects.get(id=id_pers)
    except:
        out_list = Person.objects.all()
        context = {'out_list': out_list, 'all_list':all_list}
        return render(request, 'page/all_persons.html', context)
    pers.age = str(age(pers.born))
    pers_arts = pers.article.order_by('pub_date')

    pag = Paginator(pers_arts,2)
    try:
        pagined=pag.page(page_num)
    except InvalidPage:
        pagined=pag.page(1)

    context = {'item': pers, 'all_list':all_list, 'pers_arts':pagined}
    return render(request, 'page/person.html', context)


def age (born):
# born has datetime format, like datetime.date(2011,12,31)
    today = datetime.date.today()
    return int((today.year - born.year) + ((today.month > born.month) or
    ((today.month == born.month) and (today.day >= born.day))))









