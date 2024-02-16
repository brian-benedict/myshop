from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product, Category
from decimal import Decimal





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



from django.shortcuts import render, redirect, get_object_or_404


# Update operation for Product
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'records/edit_product.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'records/delete_product.html', {'product': product})




from django.shortcuts import render, redirect
from .forms import ReservationForm

def register_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'records/register_reservation.html', {'form': form})





from django.shortcuts import render, get_object_or_404
from .models import Reservation

def reservation_list(request):
    reservations = Reservation.objects.filter(paid=False)  # Filter out paid reservations
    return render(request, 'records/reservation_list.html', {'reservations': reservations})

def reservation_payments(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    payments = reservation.reservationpayment_set.all()
    return render(request, 'records/reservation_payments.html', {'reservation': reservation, 'payments': payments})





# from django.shortcuts import render, redirect
# from .forms import ReservationPaymentForm
# from .models import Reservation

# def add_reservation_payment(request, reservation_id):
#     reservations = Reservation.objects.all()
#     reservation = Reservation.objects.get(id=reservation_id)
#     if request.method == 'POST':
#         form = ReservationPaymentForm(request.POST)
#         if form.is_valid():
#             payment = form.save(commit=False)
#             payment.reservation = reservation
#             payment.save()
#             return render(request, 'records/reservation_list.html', {'reservations': reservations})

#             # return redirect('reservation_detail', reservation_id=reservation_id)
#     else:
#         form = ReservationPaymentForm()
#     return render(request, 'records/add_reservation_payment.html', {'form': form})





# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Reservation, ReservationPayment, Sale
# from .forms import ReservationPaymentForm
# from django.utils import timezone

# def add_reservation_payment(request, reservation_id):
#     reservation = get_object_or_404(Reservation, id=reservation_id)

#     if request.method == 'POST':
#         form = ReservationPaymentForm(request.POST)
#         if form.is_valid():
#             reservation_payment = form.save(commit=False)
#             reservation_payment.reservation = reservation
#             reservation_payment.save()

#             # Create a corresponding sale entry for the product
#             product = reservation.product_reserved
#             sale_price = reservation_payment.amount  # Adjust this based on your requirements
#             sale_date = timezone.now().date()  # Assuming you're using timezone-aware dates
#             Sale.objects.create(product=product, sale_price=sale_price, sale_date=sale_date)

#             return redirect('reservation_list')
#     else:
#         form = ReservationPaymentForm()

#     return render(request, 'add_reservation_payment.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation, ReservationPayment, Sale
from .forms import ReservationPaymentForm
from django.utils import timezone

def add_reservation_payment(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    total_paid_amount = reservation.reservationpayment_set.aggregate(total_paid=Sum('amount'))['total_paid'] or 0

    if request.method == 'POST':
        form = ReservationPaymentForm(request.POST)
        if form.is_valid():
            reservation_payment = form.save(commit=False)
            reservation_payment.reservation = reservation
            reservation_payment.save()

            total_paid_amount += reservation_payment.amount

            if total_paid_amount >= reservation.target_amount:
                # Create a corresponding sale entry for the product
                product = reservation.product_reserved
                sale_price = reservation.target_amount  # Use target amount as sale price
                sale_date = timezone.now().date()  # Assuming you're using timezone-aware dates
                Sale.objects.create(product=product, sale_price=sale_price, sale_date=sale_date)

                # Remove reservation if target amount reached
                reservation.delete()

                return redirect('reservation_list')
    else:
        form = ReservationPaymentForm()

    return render(request, 'records/add_reservation_payment.html', {'form': form, 'reservation': reservation})








from django.shortcuts import render, get_object_or_404
from .models import Reservation

def reservation_detail(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    # Your view logic here...
    return render(request, 'reservation_detail.html', {'reservation': reservation})




# koleacox



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
    # Assuming you have the cost_price field in your Product model

    # Filter sales for today and annotate with total sale amount
    sales = Sale.objects.filter(sale_date__date=today).annotate(total_sale=Sum('quantity_sold'))
    for sale in sales:
        sale.profit = sale.sale_price - (sale.quantity_sold * sale.product.price_bought)

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
    for sale in sales:
        sale.profit = sale.sale_price - (sale.quantity_sold * sale.product.price_bought)

    # Retrieve expenses for the current day
    expenses = Expense.objects.filter(expense_date__date=today)
    # Calculate net income
    net_income = total_sales - total_expenses
    net_profit = sum(sale.profit for sale in sales) - total_expenses

    context = {
        'total_sales': total_sales,
        'total_expenses': total_expenses,
        'net_income': net_income,
        'sales': sales,
        'expenses': expenses,
        'net_profit': net_profit
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










# from django.shortcuts import render
# from django.http import HttpResponse
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.utils import timezone
# from records.models import Sale, Expense
# from django.db.models import Sum

# def send_daily_summary_email(request):
#     today = timezone.localdate()

#     # Retrieve total sales for the day
#     total_sales = Sale.objects.filter(sale_date__date=today).aggregate(total_sales=Sum('sale_price'))['total_sales'] or 0

#     # Retrieve total expenses for the day
#     total_expenses = Expense.objects.filter(expense_date__date=today).aggregate(total_expenses=Sum('amount'))['total_expenses'] or 0

#     # Calculate net income
#     net_income = total_sales - total_expenses

#     # Retrieve sales and expenses for the current day
#     sales = Sale.objects.filter(sale_date__date=today)
#     expenses = Expense.objects.filter(expense_date__date=today)

#     context = {
#         'total_sales': total_sales,
#         'total_expenses': total_expenses,
#         'net_income': net_income,
#         'sales': sales,
#         'expenses': expenses,
#     }

#     # Render daily summary template to HTML
#     html_content = render_to_string('records/daily_summary.html', context)

#     # Prepare email content
#     subject = f'Daily Summary - {today}'
#     recipient_list = ['brian.benedict@gretsauniversity.ac.ke']  # Replace with the owner's email

#     # Send email with HTML content
#     try:
#         send_mail(subject, '', None, recipient_list, html_message=html_content)
#         return HttpResponse('Daily summary email sent successfully')
#     except Exception as e:
#         return HttpResponse(f'Error sending daily summary email: {str(e)}')





from django.db.models import F
from django.core.mail import EmailMessage
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from records.models import Sale, Expense
from django.db.models import Sum
from django.utils import timezone

def send_daily_summary_email(request):
    today = timezone.localdate()

    # Retrieve total sales for the day
    total_sales = Sale.objects.filter(sale_date__date=today).aggregate(total_sales=Sum('sale_price'))['total_sales'] or 0

    # Retrieve total expenses for the day
    total_expenses = Expense.objects.filter(expense_date__date=today).aggregate(total_expenses=Sum('amount'))['total_expenses'] or 0

    # Calculate net income
    net_income = total_sales - total_expenses

    # Retrieve sales and expenses for the current day
    sales = Sale.objects.filter(sale_date__date=today)
    expenses = Expense.objects.filter(expense_date__date=today)
    for sale in sales:
        sale.profit = sale.sale_price - (sale.quantity_sold * sale.product.price_bought)

    net_profit = sum(sale.profit for sale in sales) - total_expenses
    # Create a PDF document
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    # Content for PDF
    elements = []

    # Add title with today's date
    title = f"Daily Summary Report - {today.strftime('%Y-%m-%d')}"
    elements.append(Paragraph(title, styles['Title']))

    # Add total sales
    elements.append(Paragraph(f"Total Sales: {total_sales}", styles['Normal']))

    # Add total expenses
    elements.append(Paragraph(f"Total Expenses: {total_expenses}", styles['Normal']))

    # Add net income
    elements.append(Paragraph(f"Net Income: {net_income}", styles['Normal']))

    elements.append(Paragraph(f"Net Profit: {net_profit}", styles['Normal']))


    products_at_minimum_quantity = Product.objects.filter(quantity_available__lte=F('minimum_quantity'))

    # Add products at minimum quantity
    if products_at_minimum_quantity.exists():
        elements.append(Paragraph("Products at Minimum Quantity:", styles['Heading2']))
        products_data = [['Name', 'Description', 'Quantity Available', 'Minimum Quantity']]
        for product in products_at_minimum_quantity:
            products_data.append([product.name, product.description, product.quantity_available, product.minimum_quantity])
        products_table = Table(products_data, colWidths=[doc.width / 4.0] * 4)  # Divide the width equally among columns
        products_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                            ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
        elements.append(products_table)





    # Add sales data in table format
    sales_data = [['Product', 'Quantity', 'Price', 'Profit']]
    for sale in sales:
        sales_data.append([sale.product.name, sale.quantity_sold, sale.sale_price, sale.profit])
    sales_table = Table(sales_data, colWidths=[doc.width / 4.0] * 4)  # Divide the width equally among columns
    sales_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                     ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                     ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                     ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                     ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                     ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(Paragraph("Sales", styles['Heading2']))
    elements.append(sales_table)

    # Add expenses data in table format
    expenses_data = [['Description', 'Amount']]
    for expense in expenses:
        expenses_data.append([expense.description, expense.amount])
    expenses_table = Table(expenses_data, colWidths=[doc.width / 2.0] * 2)  # Divide the width equally among columns
    expenses_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                        ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(Paragraph("Expenses", styles['Heading2']))
    elements.append(expenses_table)

    # Build PDF document
    doc.build(elements)

    # Get PDF content from buffer
    pdf_content = buffer.getvalue()
    buffer.close()

    # Prepare email content
    subject = f'Daily Summary Report - {today.strftime("%Y-%m-%d")}'
    body = f'Please find attached the daily summary report for {today.strftime("%Y-%m-%d")}.'
    recipient = 'brian.benedict@gretsauniversity.ac.ke'  # Replace with the owner's email

    # Send email with PDF attachment
    email = EmailMessage(subject, body, to=[recipient])
    email.attach(f'daily_summary_{today}.pdf', pdf_content, 'application/pdf')
    email.send()

    return HttpResponse('Daily summary email sent successfully')



# brian.benedict@gretsauniversity.ac.ke



