from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .import views
from django .urls import path
from cart import views
from .views import cart



urlpatterns = [
    path('',views.cart, name='cart'),





]
urlpatterns += staticfiles_urlpatterns()