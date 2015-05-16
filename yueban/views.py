from distutils.text_file import TextFile
from django_filters import FilterSet
from django_filters.filters import NumberFilter, CharFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from yueban.models import Trip, User

from yueban.serializers import TripSerializer, UserSerializer


__author__ = 'wenjuntan'

class TripFilter(FilterSet):
    startTime = NumberFilter(name="startTime", lookup_type='gte')
    finishTime = NumberFilter(name="finishTime", lookup_type='lte')
    title = CharFilter(name="title", lookup_type='contains')
    class Meta:
        model = Trip
        fields = ['title', 'destinationCity', 'destinationProvince', 'finishTime', 'startTime']


class TripListCreateView(ListCreateAPIView):
    model = Trip
    serializer_class = TripSerializer
    filter_class = TripFilter


class UserListCreateView(ListCreateAPIView):
    ##model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetailView(RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer
    print 2