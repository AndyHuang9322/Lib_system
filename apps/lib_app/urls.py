from django.conf.urls import url
from . import views
                    
urlpatterns = [
#login:
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
#dashboard:
    url(r'^quotes$', views.show),
]