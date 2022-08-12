from django import forms
from shop.models import Order, OrderDetail

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        widgets = {"customer": forms.TextInput()}
        fields = "__all__"
        
class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        widgets = {"order": forms.TextInput()}
        fields = "__all__"