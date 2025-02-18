from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser, Product
from django import forms


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name')


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'quantity']
        labels = {
            'product_name': 'Product Name',
            'description': 'Description',
            'quantity': 'Quantity'
        }
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
        }
