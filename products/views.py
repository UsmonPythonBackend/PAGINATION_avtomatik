from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from products.forms import ProductForm
from products.models import Product
from django.views.generic import ListView, DetailView
from django.contrib import messages




class ProductsView(View):
    def get(self, request):
        products = Product.objects.all().order_by('id')
        pagination = Paginator(products, 6)
        page = request.GET.get('page' 1)
        pages = pagination.page(page)
        context = {'pages': pages}
        return render(request, "shop.html", context)



class ProductDetailView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        return render(request, "shop-detail.html", {"product": product})

class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, "product_create.html", {"form": form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.slug = product.title + "001"
            product.save()
            return redirect("products-list")

