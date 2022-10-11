from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.contrib import messages
from django.urls import reverse
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return render(request, 'main/index.html')

def contact(request):
    return render(request, 'main/contact.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def gift_product(request):
    return render(request, 'main/gifts-products.html')

def design(request):
    return render(request, 'main/dizayn.html')

def printing_large(request):
    return render(request, 'main/printing-largeformat.html')

def promotional_products(request):
    return render(request, 'main/promotional-products.html')

def markirovka(request):
    return render(request, 'main/markirovka.html')

def poligraphy_product(request):
    return render(request, 'main/poligraphy-products.html')

def printing_paper(request):
    return render(request, 'main/printing-paper.html')

def printing_textile(request):
    return render(request, 'main/printing-textile.html')

def textile_products(request):
    return render(request, 'main/textile-products.html')

def advertisement(request):
    return render(request, 'main/reklama.html')

def invoice(request):
    return render(request, 'main/invoice.html')

# def application_order(request):
#     orders = OrderForm.objects.all()
#     form = OrderMForm()
#     if request.method == "POST":
#         form = OrderMForm

#     context = {'orders' : orders, 'form' : form}
#     return render(request, 'main/application_order.html', context=context)


class OrderCreateView(CreateView):
    queryset = OrderForm()
    template_name = 'application_order.html'
    fields = '__all__'
    success_url = '/application_order'

# def get_name(request):
#     if request.method == 'POST':
#         form = OrderMForm(request.POST)
#         if form.is_valid():
            
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'name.html', {'form': form})




# @csrf_exempt
# def test_form(request):
#     form = OrderMForm()
#     if request.method == 'POST':
#         form = OrderMForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {"form": form}
#     return render(request, "main/testform.html", context)


# @csrf_exempt
# def test_form(request):
#     detail = OrderForm.objects.all()
#     form = OrderMForm()
#     if request.method == 'POST':
#         form = OrderMForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {"form": form,
#                 "detail": detail
#                     }
#     return render(request, "main/application_order.html", context)




# def order(request):
#     if request.method == "POST":
#         form = OrderMForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'Reddit_app/order_thankyou.html')
#     else:
#         form = OrderMForm()
#     return render(request, 'Reddit_app/order_from_post.html', {"form": form})


@csrf_exempt
@login_required(login_url='login')
def listView(request):
    if request.user.is_authenticated:
        if OrderForm.objects.filter(manager=request.user.id):
            orders = OrderForm.objects.filter(manager=request.user.id).order_by('-id').first()
            total = 0
            all_price = orders.price * orders.amount
            percent_sum = (all_price / 100) * orders.VAT
            sum_list = all_price + percent_sum
            total = total + sum_list
            context = {}

            if orders.price1 and orders.percent1:
                all_price1 = orders.price1 * orders.number1

                percent_sum1 = (all_price1 / 100) * orders.percent1
                sum_list1 = all_price1 + percent_sum1
                total = total + sum_list1
                context['all_price1'] = all_price1
                context['sum_list1'] = sum_list1

            context['orders'] = orders
            context['sum_list'] = sum_list
            context['all_price'] = all_price
            context['total'] = total
            if orders.VAT:
                total = total + (total*orders.percent/100)
                context['total_sum']=total
        else:
            context = {}
        return render(request, 'invoice.html', context=context)



@csrf_exempt
def create(request):
    context = {}
    OrdersFormset = modelformset_factory(OrderForm, form=OrdersForm)
    form = CustomerForm(request.POST or None)
    formset = OrdersFormset(request.POST or None, queryset=OrderForm.objects.none(), prefix='orders')
    if request.method == "POST":
        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    student = form.save(commit=False)
                    student.save()

                    for order in formset:
                        data = order.save(commit=False)
                        data.student = student
                        data.save()
            except IntegrityError:
                print("Error encountered")
            
            return redirect('myprint:list')
    context = {'form' : form,'formset' : formset}
    return render(request, 'multi_forms/create.html', context=context)

def list(request):
    datas = Customer.objects.all()
    context = {'datas' : datas}
    return render(request, 'multi_forms/list.html', context=context)


class Home(TemplateView):
    template_name = 'all.html'
