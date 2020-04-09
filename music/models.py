from django.db import models

# Create your models here.

class Musician(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Song(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name 
        
class Album(models.Model):
    name = models.CharField(max_length=100)

    
    def __str__(self):
        return self.name 