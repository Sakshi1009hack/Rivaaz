from django.shortcuts import render,redirect
from core2.forms import *
# Create your views here.
def index(request):
    return render(request,'core/index.html')

def add_product(request):
    if request == 'POST':
        form= ProductForm(request.POST)
        if form.is_valid():
         form.save()
        return redirect('/')
    else:
        form = ProductForm()
      
    return render(request,'core/add_product.html',{'form':form})