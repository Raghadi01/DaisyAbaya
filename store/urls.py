from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views
from django.urls import path, include
from .views import home

from .views import products


from store import views
from django.urls import path



urlpatterns = [

   path('', views.home, name='home'),
   path('products/', views.products, name='products'),
   path(' AbayaDetails1/', views. AbayaDetails1, name='AbayaDetails1'),
   path(' AbayaDetails2/', views.AbayaDetails2, name='AbayaDetails2'),
   path(' AbayaDetails3/', views.AbayaDetails3, name='AbayaDetails3'),
   path(' AbayaDetails4/', views.AbayaDetails4, name='AbayaDetails4'),










]

