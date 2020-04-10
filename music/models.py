from django.db import models
# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)
    publish_date = models.DateField(null=True)

    # allows us to see the objects as a string
    def __str__(self):
        return self.name 

class Song(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    num_stars = models.IntegerField()

    # allows us to see the objects as a string
    def __str__(self):
        return self.name 


class Creator(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    member = models.ManyToManyField("Creator", through=("Subscription"))

    def __str__(self):
        return self.name

class Subscription(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    day_joined = models.DateField(null=True)

