from django.contrib import admin

# Register your models here.

from page.models import Article, Reporter, Person
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Person)
