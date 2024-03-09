from django.shortcuts import render
from .models import Product
# Create your views here.
def productview(request):
    pro=Product.object.all()
    return render(request,'index.html',{'pro':pro})