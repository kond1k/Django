import datetime
from .models import ProductCategory, Product, Contact
from django.conf import settings
import random

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket


def main(request):
    title = "главная"
    products = Product.objects.all()

    content = {"title": title, "products": products}
    return render(request, "mainapp/index.html", content)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return[]


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_product(hot_product):
    same_products = Product.objects.filter(
        category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def products(request, pk=None):
    title = "продукты"
    links_menu = ProductCategory.objects.all()

    basket = get_basket(request.user)
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by("price")
            category = {"name": "все"}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(
                category__pk=pk).order_by("price")
        content = {"title": title, "links_menu": links_menu, "category": category,
                   "products": products, "media_url": settings.MEDIA_URL, "basket": basket, }
        return render(request, "mainapp/products_list.html", content)
    hot_product = get_hot_product()
    same_products = get_same_product(hot_product)
    content = {"title": title, "links_menu": links_menu,
               "same_products": same_products, "media_url": settings.MEDIA_URL, "hot_product": hot_product, }
    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date,
               "locations": locations}
    return render(request, "mainapp/contact.html", content)
