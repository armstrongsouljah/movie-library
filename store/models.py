from django.db import models
from utils.helpers import generate_slug
from django.db.models.signals import pre_save


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=145, blank=False, null=False,  
                             unique=True)
    movie_slug = models.CharField(blank=True, max_length=250)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


def pre_save_receiver(instance, *args, **kwargs):
    if not instance.movie_slug:
        instance.movie_slug = generate_slug(instance.title)


pre_save.connect(pre_save_receiver, sender=Movie)
