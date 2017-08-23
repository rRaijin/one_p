from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *


def landing(request):
    name = "Raijin"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()

    return render(request, 'landing/landing.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category=1)
    products_images_laptops = products_images.filter(product__category=4)
    products_images_clocks = products_images.filter(product__category=5)
    products_images_notebooks = products_images.filter(product__category=3)
    products_images_ears = products_images.filter(product__category=2)
    return render(request, 'landing/home.html', locals())




