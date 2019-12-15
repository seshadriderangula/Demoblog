from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'index',views.index,name='index'),
    url(r'contact$', views.contact, name='contact'),
    url(r'portfolia$', views.portfolia, name='portfolia'),
    url(r'send$',views.send, name='send'),
    url(r'register$',views.register, name='register')
]