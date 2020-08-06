from django.db import models
from random import randint
from django.db.models import Count

# Create your models here.


class QuotesManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0,count - 1)
        return self.all()[random_index]

class Quote(models.Model):
    objects = QuotesManager()
    series = models.CharField(max_length=100,blank=True)
    character = models.CharField(max_length=100, blank=True)
    quote = models.TextField()
    episode = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.quote}\n - **{self.character}**, *{self.series}*"
