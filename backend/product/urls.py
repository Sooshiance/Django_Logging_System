from django.urls import path

from product.views import allProducts


urlpatterns = [
    path('', allProducts, name='products'),
]
