from django.db import models
from datetime import datetime

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=225, null=True)
    last_name = models.CharField(max_length=225, null=True)
    age = models.IntegerField(null=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Song(models.Model):
    artiste_ID = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=225, null=True)
    date_released = models.DateTimeField(default=datetime.today)
    likes = models.IntegerField(null=True)
    
    def __str__(self):
        return self.title

class Lyric(models.Model):
    sond_ID = models.ForeignKey(Song,  on_delete=models.CASCADE)
    content = models.TextField(max_length=500, null=True)
    
    def __str__(self):
        return self.content[:20] + '...'