from django.conf.urls import url
from . import views
                    
urlpatterns = [
#login:
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
#dashboard:
    url(r'^quotes$', views.show),
    url(r'^post/(?P<id>\d+)$', views.add_book),
    url(r'^like/(?P<id>\d+)/(?P<book>\d+)$', views.like),
    url(r'^edit_book/(?P<id>\d+)$', views.edit_book),
    url(r'^delete/(?P<id>\d+)$', views.delete),  
    url(r'^back/', views.back),
]