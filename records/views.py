from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
    return render(request, 'records/product_list.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'records/product_detail.html', {'product': product})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'records/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    products = category.products.all()
    return render(request, 'records/category_detail.html', {'category': category, 'products': products})




from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'records/add_product.html', {'form': form})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'records/add_category.html', {'form': form})
