from django.shortcuts import render
from cart.models import Product

# Create your views here.
def rehomepage(request):
    pro = Product.objects.all()
    return render(request, 'index.html', {'pros':pro})

