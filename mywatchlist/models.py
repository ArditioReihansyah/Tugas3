from platform import release
from django.db import models

# Create your models here.
class watchlist(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    deskripsi = models.TextField()