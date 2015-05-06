__author__ = 'wenjuntan'

from django.db import models

class Trip (models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    destinationCountry = models.CharField(max_length= 200, default='China')
    destinationProvince = models.CharField(max_length= 200)
    destinationCity = models.CharField(max_length= 200)
    fromCountry = models.CharField(max_length= 200, default='China')
    fromProvince = models.CharField(max_length= 200)
    fromCity = models.CharField(max_length= 200)
    startingTime = models.DateTimeField()
    endingTime = models.DateTimeField()
    picture = models.TextField(blank = True)

    info = models.TextField(blank = True)
    #owner = models.ForeignKey(User)

    class Meta:
        ordering = ('created',)

class User (models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length= 200)
    password = models.CharField(max_length= 200)
    picture = models.TextField()
    email = models.EmailField(blank=True)
    info = models.TextField()
    gender = models.CharField(max_length=1, choices=(('F','F'),('M', 'M')))
    age = models.SmallIntegerField(blank=True)
    province = models.CharField(max_length= 200, blank=True)
    country = models.CharField(max_length= 200, default='China')
    city = models.CharField(max_length= 200, blank=True)


