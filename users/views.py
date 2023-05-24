from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm


from . import forms



# Create your views here.

def login(request):
    return render(request, 'users/login.html')





def signup(requset):
    if requset.method == 'POST':
        form =  UserRegistrationForm(requset.POST)
        if form.is_valid():
            form.save()

            messages.success(requset, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form =  UserRegistrationForm()

    context = {'form': form}
    return render(requset, 'users/signup.html', context)







