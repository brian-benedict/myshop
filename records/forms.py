from django import forms
from .models import Product, Category



from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'price_bought', 'quantity_available', 'category']



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']



from django import forms
from .models import Sale

class SaleForm(forms.ModelForm):
    sale_price = forms.DecimalField(label='Sale Price')  # Add this field

    class Meta:
        model = Sale
        fields = ['product', 'quantity_sold', 'sale_price']  # Include 'sale_price'



from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = ['expense_date']  # Exclude 'expense_date' field from the form
