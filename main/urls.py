from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='home'),
    path('Announcements', views.about, name='about')
      
]
