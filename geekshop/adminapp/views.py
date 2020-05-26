from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings

from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory

# Create your views here.


def admin_main(request):
    response = redirect("admin:users")
    return response


def users(request):
    title = "админка/пользователи"
    users_list = ShopUser.objects.all().order_by(
        "-is_active", "-is_superuser", "-is_staff", "username")
    content = {"title": title, "objects": users_list,
               "media_url": settings.MEDIA_URL}
    return render(request, "adminapp/users.html", content)


def user_create(request):
    response = redirect("admin:users")
    return response


def user_update(request, pk):
    response = redirect("admin:users")
    return response


def user_delete(request, pk):
    response = redirect("admin:users")
    return response


def categories(request):
    title = "админка/категории"
    categories_list = ProductCategory.objects.all()
    content = {"title": title, "objects": categories_list,
               "media_url": settings.MEDIA_URL}
    return render(request, "adminapp/categories.html", content)


def category_create(request):
    response = redirect("admin:categories")
    return response


def category_update(request, pk):
    response = redirect("admin:categories")
    return response


def category_delete(request, pk):
    response = redirect("admin:categories")
    return response


def products(request, pk):
    title = "админка/продукт"
    category = get_object_or_404(ProductCategory, pk=pk)
    product_list = Product.objects.filter(category__pk=pk).order_by("name")
    content = {"title": title, "category": category, "objects": product_list,
               "media_url": settings.MEDIA_URL}
    return render(request, "adminapp/products.html", content)


def product_create(request, pk):
    response = redirect("admin:categories")
    return response


def product_read(request, pk):
    response = redirect("admin:categories")
    return response


def product_update(request, pk):
    response = redirect("admin:categories")
    return response


def product_delete(request, pk):
    response = redirect("admin:categories")
    return response
