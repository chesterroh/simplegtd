from django.conf.urls import url

from . import views
app_name = 'logaqi'
urlpatterns = [
    url(r'^aqiapi/$',views.aqiapi,name='aqiapi'),
]
