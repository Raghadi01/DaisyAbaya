from django.urls import path
from .import views
from users import  views
from django.contrib.auth import views as auth_views

from users import views as user_views

from django.contrib.auth import views as auth_views

from users import views as user_views


urlpatterns = [
    path('signup/', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]
