from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request,'homepage.html')

def error_page(request):
    return render(request,'base.html')