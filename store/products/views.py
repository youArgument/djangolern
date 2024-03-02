from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title':'My App',
        'is_promotion': False,
    }
    return render(request, 'products/index.html',context)


def products(request):
    return  render(request,'products/products.html')