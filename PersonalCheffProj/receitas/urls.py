from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sucodelaranja', views.sucodelaranja, name='sucodelaranja'),
    path('sucodelimao', views.sucodelimao, name='sucodelimao'),
    path('sucodeabacaxi', views.sucodeabacaxi, name='sucodeabacaxi'),
    path('sucodemaca', views.sucodemaca, name='sucodemaca'),
    path('sucodemelancia', views.sucodemelancia, name='sucodemelancia')
]