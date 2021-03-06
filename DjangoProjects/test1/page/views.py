from django.shortcuts import render
from .models import Article, Reporter, Person
from django.core.paginator import Paginator, InvalidPage, PageNotAnInteger
import datetime
from django.views.generic.base import TemplateView, ContextMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ProcessFormView
from django.core.urlresolvers import reverse, reverse_lazy






# Create your views here.

class AllListMixin (ContextMixin):
    def get_context_data (self, **kwargs):
       context = super(AllListMixin, self).get_context_data(**kwargs)
       context['all_list'] = whole_list()
       return context



'''
def test (request, test_id):
    all_list = whole_list()
    test_list=[]
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
'''

class TestView (ListView):
    template_name = 'page/test.html'
    context_object_name='test_list'
    def get (self, request, *args, **kwargs):
        self.test_list=[]
        # строка приема неименованных аргументов. Соотвествует закомментированной строке в url
        #для работы строку раскомментить, взамен закоментить расположенную ниже. Вместе не работают из-за несовсместимости
        # в url args и kwargs

        #self.test_list.append(self.args[0])
        self.test_list.append(self.kwargs['test'])
        try:
            get_par = request.GET['id']
            get_par = str(get_par)
            self.test_list.append(get_par)
        except: pass
        try:
            get_par = request.GET['page_num']
            get_par = str(get_par)
            self.test_list.append(get_par)
        except: pass

        return super(TestView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        return self.test_list

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        context['all_list'] = whole_list()
        return context


class ArticleView(TemplateView):
    def get_context_data(self, **kwargs):
        context=super(ArticleView,self).get_context_data(**kwargs)
        all_list=whole_list()
        context['all_list'] = all_list
        art = Article.objects.get(id=kwargs['id_art'])
        context['art']=art
        pers_set = art.person_set.all()
        pers_list = []
        for item in pers_set:
            item.age = str(age(item.born))
            pers_list.append(item)
        pag = Paginator(pers_list, 2)
        try:
            pagined = pag.page(kwargs['page_num'])
        except InvalidPage:
            pagined = pag.page(1)
        context['pers_list']=pagined

        return context


class AllArticleView(ArchiveIndexView, AllListMixin):
    template_name = 'page/all_articles.html'
    model = Article
    date_field = 'pub_date'

    def get_context_data(self, **kwargs):
        context = super(AllArticleView, self).get_context_data(**kwargs)
        #context['all_list'] = whole_list() вынесено в класс AllListMixin
        return context
'''
class ReporterView(TemplateView):
    template_name = 'page/reporter.html'
    def get_context_data(self, **kwargs):
        context=super(ReporterView,self).get_context_data(**kwargs)
        out_list=[]
        if kwargs:
            rep = Reporter.objects.get(id=kwargs['id_rep'])
            out_list.append(rep)
            art_set = rep.article_set.all()
            for item in art_set:
                out_list.append(item)
            context['out_list']=out_list
        else:
            out_list=Reporter.objects.all()
            context['out_list']=out_list

        all_list=whole_list()
        context['all_list']=all_list
        return context
'''

class ReporterView(DetailView):
    template_name = 'page/reporter.html'
    queryset = Reporter.objects.all()
    pk_url_kwarg = 'id_rep'
    context_object_name = 'reporter'

    def get (self, request, *args, **kwargs):
        self.rep = Reporter.objects.get(id=self.kwargs['id_rep'])
        self.arts = self.rep.article_set.all()
        return super(DetailView, self).get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ReporterView, self).get_context_data(**kwargs)
        context['out_list'] = self.arts
        context['all_list'] = whole_list()
        return context

class AllReporterView(YearArchiveView):
    template_name = 'page/all_reporters.html'
    model = Reporter
    date_field = 'work_begin'
    make_object_list = True
    #object_list = 'out_list' # не работает сцуко, можно только object_list в  шаблоне
    year = '2015'  #можно сделать 2015, будет 1 репортер

    def get_context_data (self, **kwargs):
       context = super(AllReporterView, self).get_context_data(**kwargs)
       context['all_list'] = whole_list()
       return context


'''

#если раскомментировать, надо убрать year из шаблона

class AllReporterView(ListView):
    template_name = 'page/all_reporters.html'
    queryset = Reporter.objects.all()



    def get_context_data (self, **kwargs):
       context = super(AllReporterView, self).get_context_data(**kwargs)

       context['all_list'] = whole_list()
       return context
'''



def index(request):
    all_list=whole_list()
    context = {'all_list': all_list}
    return render(request, 'page/index.html', context)


class PersonView(ListView, AllListMixin):

    def get (self, request, *args, **kwargs):
        self.pers = Person.objects.get(id=self.kwargs['id_pers'])
        self.pers.age = str(age(self.pers.born))
        return super(PersonView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        return self.pers.article.order_by('pub_date')

    paginate_by=2

    def get_context_data (self, **kwargs):
       context = super(PersonView, self).get_context_data(**kwargs)
       context['item']=self.pers
      # context['all_list'] = whole_list() вынесено в класс AllListMixin
       return context



class AllPersonView(ListView):

    def get_queryset(self):
        return Person.objects.all()

    context_object_name = 'out_list'

    def get_context_data (self, **kwargs):
       context = super(AllPersonView, self).get_context_data(**kwargs)

       context['all_list'] = whole_list()

       return context




def age (born):
# born has datetime format, like datetime.date(2011,12,31)
    today = datetime.date.today()
    return int((today.year - born.year) + ((today.month > born.month) or
    ((today.month == born.month) and (today.day >= born.day))))



def whole_list():
    all_list=[]
    all_list.append(Reporter.objects.all())
    all_list.append(Article.objects.all())
    all_list.append(Person.objects.all())
    return all_list


class CbvView(ListView):

    queryset=Person.objects.all()
    context_object_name = 'the_list'
    def get_context_data(self,**kwargs):
        context = super(CbvView, self).get_context_data(**kwargs)
        all_list=whole_list()
        context['all_list']=all_list
        return context

'''

    def get_queryset(self):
        return Person.objects.all()
'''


'''
class RepEditMixin (AllListMixin):
    def get_context_data(self,**kwargs):
        context = super(RepEditMixin, self).get_context_data(**kwargs)

        return context

class RepEditView (ProcessFormView):
    def post (self, request, *args, **kwargs):

        return super(RepEditView, self).post(request, *args, **kwargs)
'''
class RepCreate (CreateView, AllListMixin):
    model = Reporter
    fields = ['full_name', 'weight', 'height', 'wage', 'work_begin']
    template_name = 'page/add.html'

    def get_success_url(self):
        return reverse('page_app:reporter', kwargs={'id_rep': self.object.id})

    #success_url = reverse_lazy('page_app:reporters') взаимозаменяемо с self.success_url из def post
    '''
    def get (self, request, *args, **kwargs):   #нужна только для initial значенией в полях
        self.initial['full_name'] = 'New reporter name'
        return super(RepCreate, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        #  self.success_url = reverse('page_app:reporter') #не работает с kwargs
        return super(RepCreate, self).post(request, *args, **kwargs)
'''
    def get_context_data(self, **kwargs):
        context = super(RepCreate, self).get_context_data(**kwargs)
        context['model_name'] = 'Reporter'
        return context


class RepUpdate(UpdateView, AllListMixin):
    model = Reporter
    fields = ['full_name', 'weight', 'height', 'wage', 'work_begin']
    template_name = 'page/update.html'
    pk_url_kwarg = 'id_rep'

    def get_success_url(self):
        return reverse('page_app:reporter', kwargs={'id_rep': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(RepUpdate, self).get_context_data(**kwargs)
        context['model_name'] = 'Reporter'
        return context

class RepDelete(DeleteView, AllListMixin):
    model = Reporter
    fields = ['full_name', 'weight', 'height', 'wage', 'work_begin']
    template_name = 'page/delete.html'
    pk_url_kwarg = 'id_rep'
    success_url = reverse_lazy('page_app:reporters')

    def get_context_data(self, **kwargs):
        context = super(RepDelete, self).get_context_data(**kwargs)
        context['model_name'] = 'Reporter'
        return context



class ArtCreate (CreateView, AllListMixin):
    model = Article
    fields = ['headline', 'pub_date', 'content', 'reporter']
    template_name = 'page/add.html'

    def get_success_url(self):
        return reverse('page_app:article', kwargs={'id_art': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(ArtCreate, self).get_context_data(**kwargs)
        context['model_name'] = 'Article'
        return context


class ArtUpdate(UpdateView, AllListMixin):
    model = Article
    fields = ['headline', 'pub_date', 'content', 'reporter']
    template_name = 'page/update.html'
    pk_url_kwarg = 'id_art'

    def get_success_url(self):
        return reverse('page_app:article', kwargs={'id_art': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(ArtUpdate, self).get_context_data(**kwargs)
        context['model_name'] = 'Article'
        return context

class ArtDelete(DeleteView, AllListMixin):
    model = Article
    fields = ['headline', 'pub_date', 'content', 'reporter']
    template_name = 'page/delete.html'
    pk_url_kwarg = 'id_art'
    success_url = reverse_lazy('page_app:articles')

    def get_context_data(self, **kwargs):
        context = super(ArtDelete, self).get_context_data(**kwargs)
        context['model_name'] = 'Article'
        return context

class PersCreate (CreateView, AllListMixin):
    model = Person
    fields = ['name', 'article', 'born']
    template_name = 'page/add.html'

    def get_success_url(self):
        return reverse('page_app:persone', kwargs={'id_pers': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PersCreate, self).get_context_data(**kwargs)
        context['model_name'] = 'Person'
        return context

class PersUpdate(UpdateView, AllListMixin):
    model = Person
    fields = ['name', 'article', 'born']
    template_name = 'page/update.html'
    pk_url_kwarg = 'id_pers'

    def get_success_url(self):
        return reverse('page_app:persone', kwargs={'id_pers': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PersUpdate, self).get_context_data(**kwargs)
        context['model_name'] = 'Persone'
        return context

class PersDelete(DeleteView, AllListMixin):
    model = Person
    fields = ['name', 'article', 'born']
    template_name = 'page/delete.html'
    pk_url_kwarg = 'id_pers'
    success_url = reverse_lazy('page_app:persones')

    def get_context_data(self, **kwargs):
        context = super(PersDelete, self).get_context_data(**kwargs)
        context['model_name'] = 'Persone'
        return context

