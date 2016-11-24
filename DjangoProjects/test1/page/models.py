from django.db import models

# Create your models here.
#SELECT * FROM INFORMATION_SCHEMA.TABLES where table_name LIKE 'page%'
#SELECT * FROM page_article

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)
    weight = models.IntegerField()
    height = models.IntegerField()
    wage = models.IntegerField()
    work_begin = models.DateField()

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    def __str__(self):
        out_str=self.headline
        return out_str


class Person (models.Model):
    name = models.CharField(max_length=70)
    article = models.ManyToManyField(Article)
    born = models.DateField()
    def __str__(self):
        out_str = self.name
        return out_str




