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
     url(r'^post/(?P<id>\d+)$', views.add_book)
]