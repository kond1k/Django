import datetime
import random

from .models import ProductCategory, Product, Contact
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def main(request):
    title = "главная"
    products = Product.objects.all()

    content = {"title": title, "products": products,
               "media_url": settings.MEDIA_URL}
    return render(request, "mainapp/index.html", content)


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_product(hot_product):
    same_products = Product.objects.filter(
        category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def products(request, pk=None, page=1):
    title = "продукты"
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == '0':
            category = {"pk": 0, "name": "все"}
            products = Product.objects.filter(
                is_active=True, category__is_active=True).order_by("price")
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(
                category__pk=pk, is_active=True, category__is_active=True).order_by("price")
        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {"title": title, "links_menu": links_menu, "category": category,
                   "products": products_paginator, "media_url": settings.MEDIA_URL, }
        return render(request, "mainapp/products_list.html", content)
    hot_product = get_hot_product()
    same_products = get_same_product(hot_product)
    content = {"title": title, "links_menu": links_menu,
               "same_products": same_products, "media_url": settings.MEDIA_URL, "hot_product": hot_product, }
    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/products.html", content)


def product(request, pk):
    title = "Продукты"
    content = {
        "title": title,
        "links_menu": ProductCategory.objects.all(),
        "product": get_object_or_404(Product, pk=pk),
        "media_url": settings.MEDIA_URL,
    }
    return render(request, "mainapp/product.html", content)


def contact(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date,
               "locations": locations}
    return render(request, "mainapp/contact.html", content)
