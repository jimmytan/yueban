from django.conf.urls import patterns, include, url
from django.contrib import admin
from yueban.views import UserDetailView, UserListCreateView

user_urls = patterns('',
                     url(r'^/(?P<pk>\d+)$', UserDetailView.as_view(), name='user-detail'),
                     url(r'^$', UserListCreateView.as_view(), name='user-list'))

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yueban.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^users', include(user_urls)),
    url(r'^', include('yueban.urls')),
)
