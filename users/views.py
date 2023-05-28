from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Contant



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



def contact(requset):
    if requset.method == 'POST':
        v_name= requset.POST.get('name')
        v_email= requset.POST.get('email')
        v_subject= requset.POST.get('subject')
        v_massage= requset.POST.get('massage')


        v_contact=Contant(name=v_name,email=v_email,subject=v_subject,massage=v_massage)

        v_contact.save()
        return render(requset,'users/thankyou.html')


    else:
     return render(requset,'users/contact.html')





