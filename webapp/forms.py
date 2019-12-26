from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, NumberInput
from webapp.models import Product


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Name',
        }
        error_messages = {
            'username': {
                'max_length': ("This user's name is too long.")
            }
        }
        widgets = {
            'username': TextInput({'class': 'form-control'}),
            'password': PasswordInput({'class': 'form-control'})
        }
    username_validator = User.username_validator


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'interest_rate', 'min_date', 'max_date', 'sum', 'early_repayment']
        labels = {
            'name': 'Title',
            'interest_rate': 'Interest rate, %',
            'min_date': 'Minimum term, month',
            'max_date': 'Maximum term, month',
            'sum': 'Summa',
            'early_repayment': 'Early Repayment'
        }
        widgets = {
        }