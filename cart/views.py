from django.shortcuts import render
from . import views

from django.shortcuts import render, redirect
from django.contrib import messages




def cart(reqeust):
    return render(reqeust, 'cart/cart.html')
