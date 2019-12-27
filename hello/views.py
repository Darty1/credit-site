import os

import requests
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Product


# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import ListView


def index(request: HttpRequest):
    from .forms import ProductForm
    return render(request, 'home.html', {'form': ProductForm()})


def logout(request: HttpRequest):
    from django.contrib.auth import logout
    logout(request)
    return redirect(reverse('index'))


class ShowProduct(View):
    def get(self, request, product_id):
        from django.db.models import ObjectDoesNotExist
        try:
            product = Product.objects.get(pk=product_id)
            payment = round(product.sum*((product.interest_rate / 100 / 12) * (1 + (product.interest_rate / 100 / 12)) ** product.max_date / ((1 + product.interest_rate / 100 / 12) ** product.max_date - 1)), 2)
            sum = product.sum
            procent = []
            body = []
            number = []
            for i in range(product.max_date):
                procent.append(round(sum*product.interest_rate/100/12, 2))
                body.append(round(payment-procent[i], 2))
                sum = sum - body[i]
                number.append(i+1)
            table = zip(number, procent, body)
        except ObjectDoesNotExist:
            return HttpResponseNotFound
        return render(request, 'product.html',
                      {'product': product, 'payment': payment, 'table': table})


class SeacrhView(ListView):
    model = Product
    template_name = 'seacrh_results.html'

    def get_queryset(self):  # новый
        min_date = self.request.GET.get('min_date')
        max_date = self.request.GET.get('max_date')
        sum = self.request.GET.get('sum')
        early_repayment = self.request.GET.get('early_repayment')
        if early_repayment == 'on':
            early_repayment = True
        else:
            early_repayment = False
        object_list = Product.objects.filter(min_date__icontains=min_date, max_date__icontains=max_date,
                                             sum__icontains=sum, early_repayment__icontains=early_repayment)
        return object_list


class CreateView(View):

    def get(self, request: HttpRequest):
        from .forms import ProductForm
        return render(request, 'create_page.html', {'form': ProductForm()})

    def post(self, request):
        from .forms import ProductForm
        name = request.POST['name']
        interest_rate = request.POST['interest_rate']
        min_date = request.POST['min_date']
        max_date = request.POST['max_date']
        sum = request.POST['sum']
        early_repayment = False
        if request.POST['early_repayment'] == None:
            early_repayment = False
        else:
            early_repayment = True
        from .models import Product
        product = Product(name=name, interest_rate=interest_rate, min_date=min_date, max_date=max_date,
                          sum=sum, early_repayment=early_repayment)
        product.save()
        return render(request, 'create_page.html', {'form': ProductForm()})


class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        from .forms import UserForm
        return render(request, 'login.html', {'form': UserForm()})

    def post(self, request: HttpRequest) -> HttpResponse:
        from django.contrib.auth import authenticate, login
        from django.contrib.auth.models import User
        from .forms import UserForm
        username = request.POST['username']
        password = request.POST['password']
        user: User = authenticate(request, username=username, password=password)
        if not user:
            return render(request, 'index.html', {'form': UserForm(), 'error': True})
        login(request, user)
        return redirect(reverse('index'))


class RegisterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        from .forms import UserForm
        return render(request, 'register.html', {'form': UserForm()})

    def post(self, request: HttpRequest) -> HttpResponse:
        from django.contrib.auth import login
        from .forms import UserForm

        form = UserForm(request.POST)
        if not form.is_valid():
            return render(request, 'register.html', {'form': UserForm(), 'error': True})
        try:
            username = form.data['username']
            password = form.data['password']
            user = User.objects.create_user(username=username, password=password)
        except:
            return render(request, 'register.html', {'form': UserForm(), 'error': True})
        login(request, user)
        return redirect(reverse('index'))
