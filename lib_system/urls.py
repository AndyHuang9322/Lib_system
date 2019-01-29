from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.lib_app.urls'))
]