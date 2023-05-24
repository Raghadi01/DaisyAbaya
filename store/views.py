from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request, 'store/home.html')


def products(requset):
    return render(requset, 'store/products.html')


def AbayaDetails1(requset):
    return render(requset, 'store/AbayaDetails1.html')


def AbayaDetails2(requset):
    return render(requset, 'store/AbayaDetails2.html')


def AbayaDetails3(requset):
    return render(requset, 'store/AbayaDetails3.html')


def AbayaDetails4(requset):
    return render(requset, 'store/AbayaDetails4.html')





