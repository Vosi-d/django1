from django.db import models

class Article(models.Model):
    title = models.CharField('name', max_length=250)
    intro = models.CharField('anons', max_length=250)
    full_text = models.TextField('post')
    date = models.DateTimeField('date of post')


    def __str__(self):
        return self.title