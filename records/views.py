from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product, Category






def home(request):
    return render(request, 'home.html')



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
            return redirect('product_list')  # Redirect to the product list page after adding a product
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




from django.shortcuts import render, redirect
from .forms import SaleForm

def record_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_success')  # Redirect to a success page
    else:
        form = SaleForm()
    return render(request, 'records/record_sale.html', {'form': form})

def sale_success(request):
    return render(request, 'records/sale_success.html')









from django.shortcuts import render
from django.db.models import Sum
from .models import Sale

def daily_sales(request):
    # Get today's date
    today = timezone.now().date()
    
    # Filter sales for today and annotate with total sale amount
    sales = Sale.objects.filter(sale_date__date=today).annotate(total_sale=Sum('quantity_sold'))
    
    context = {
        'sales': sales,
    }
    
    return render(request, 'records/daily_sales.html', context)












from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from .models import Expense



# def daily_summary(request):
#     today = timezone.localdate()  # Get today's date in the current time zone
    
#     # Filter expenses for today and calculate total expenses
#     expenses = Expense.objects.filter(expense_date__date=today)
#     total_expenses = expenses.aggregate(total_expenses=Sum('amount'))['total_expenses'] or 0

#     context = {
#         'expenses': expenses,
#         'total_expenses': total_expenses,
#     }
    
#     return render(request, 'records/daily_summary.html', context)






def daily_summary(request):
    today = timezone.now().date()  # Get the current date
    # Get total sales for the day
    total_sales = Sale.objects.filter(sale_date__date=today).aggregate(total_sales=Sum('sale_price'))['total_sales'] or 0

    # Get total expenses for the day
    total_expenses = Expense.objects.filter(expense_date__date=today).aggregate(total_expenses=Sum('amount'))['total_expenses'] or 0
    sales = Sale.objects.filter(sale_date__date=today)

    # Retrieve expenses for the current day
    expenses = Expense.objects.filter(expense_date__date=today)
    # Calculate net income
    net_income = total_sales - total_expenses

    context = {
        'total_sales': total_sales,
        'total_expenses': total_expenses,
        'net_income': net_income,
        'sales': sales,
        'expenses': expenses,
    }

    return render(request, 'records/daily_summary.html', context)






from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import ExpenseForm

def record_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.expense_date = timezone.now()  # Set expense_date to current date and time
            expense.save()
            # Redirect to a success page or another page as needed
            return redirect('daily_summary')  # Redirect to daily summary after recording expense
    else:
        form = ExpenseForm()
    return render(request, 'records/record_expense.html', {'form': form})





def expenses_summary(request):
    today = timezone.localdate()  # Get today's date in the current time zone

    # Filter expenses for today
    expenses = Expense.objects.filter(expense_date__date=today)

    context = {
        'expenses': expenses,
    }

    return render(request, 'records/expenses_summary.html', context)
