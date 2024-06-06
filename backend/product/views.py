from django.shortcuts import render

from product.models import Product


def allProducts(request):
    p = Product.objects.all()
    request.query = p
    return render(request, "product/home.html", {'products':p})
