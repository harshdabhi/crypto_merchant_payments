from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from payment_repo.pay import payments

# Create your views here. 


def homepage(request): 
    if request.method=='POST':
        payment_mode=request.POST.get('payment')
        print(payment_mode) 
        p_=payments() 
        return redirect('./qr_code')
        


    return render(request,'homepage.html')

def qr_code(request):
    return render(request,'qr_code.html')

def error_page(request):
    return render(request,'base.html') 