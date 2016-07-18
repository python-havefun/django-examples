from django.conf.urls import url

from . import views
app_name='first'
urlpatterns=[
    url(r'^$',views.details,name='details'),
    url(r'^(?P<question_id>[0-9]+)/$',views.index,name='index'),
    
    
    ]
