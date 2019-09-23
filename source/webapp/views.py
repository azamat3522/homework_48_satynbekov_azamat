from django.shortcuts import render, get_object_or_404

# Create your views here.
from webapp.models import Product


def index_view(request):
    products = Product.objects.filter(balance__gt=0).order_by('name', 'category')
    return render(request, 'index.html', context={
        'products': products
    })


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product.html', context={
        'product': product
    })


def product_search(request):
    value = request.GET.getlist('search')
    products = Product.objects.filter(name__in=value)
    return render(request, 'index.html', context={
        'products': products
    })
