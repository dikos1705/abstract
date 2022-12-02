from django.db import models

# Create your models here.
class Actors (models.Model):
    name = models.CharField(max_length=200)
    is_star = models.BooleanField(default=False)


    def __str__(self):
        return self.name
        