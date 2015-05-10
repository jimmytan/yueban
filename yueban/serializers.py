from rest_framework import serializers
from yueban.models import Trip, User

__author__ = 'wenjuntan'

class TripSerializer(serializers.ModelSerializer):
    class Meta:

        model = Trip
        fields =('id','title', 'destinationCountry', 'destinationProvince',
                 'destinationCity', 'fromCountry', 'fromProvince',
                    'fromCity', 'startingTime', 'endingTime', 'info')
        read_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'userName', 'password', 'email', 'info', 'gender', 'age', 'province',
                  'city', 'country')
        read_only_fields=('id',)