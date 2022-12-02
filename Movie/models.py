from django.db import models
from actors.models import Actors
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    actors = models.ManyToManyField(Actors, blank=True)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title
    

    class Meta:
        abstract = True


class Film (Movie):
    length = models.CharField(max_length= 30)

    def __str__(self):
        return self.title

class Commercial(Movie):
    company = models.CharField(max_length = 40)

    def __str__(self):
        return self.title
    
    