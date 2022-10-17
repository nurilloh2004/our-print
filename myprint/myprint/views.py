from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.contrib import messages
from django.urls import reverse
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import  authenticate
from django.contrib.auth import login as auth_login
# Create your views here.

def home(request):
    print(" ppp ---------->>>>>",request.user)
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


class OrderCreateView(CreateView):
    queryset = OrderForm()
    template_name = 'application_order.html'
    fields = '__all__'
    success_url = '/application_order'













def listview(request):
    datas = OrderForm.objects.all()
    dataform = Customer.objects.all()
    context = {'datas' : datas,'dataform' : dataform}
    return render(request, 'multi_forms/list.html', context=context)



@csrf_exempt
def createView(request):
    context = {}
    print("ppppp -------------->>>>>", request.POST)
    OrdersFormset = modelformset_factory(OrderForm, form=OrdersForm)
    print("order form set", OrdersFormset)
    form = CustomerForm(request.POST or None)
    
    formset = OrdersFormset(request.POST or None, queryset=OrderForm.objects.none(), prefix='orders')
    print(len(formset.forms), "---------.-.-.-.-.-.-.-.-.----")

    for formm in formset:
        print("*********************", formm.as_table())
    if request.method == "POST":
        if form.is_valid() and formset.is_valid():
            print(formset)
            try:
                with transaction.atomic():
                    student = form.save(commit=False)
                    student.save()
                if len(formset) > 1:
                    for order in formset:
                        data = order.save(commit=False)
                        data.student = student
                        data.save()
                else:

                    dt = OrderForm()
                    dt.name = formset[0]['name']
                    print(formset[0]['name'], "------------------------------")
                    print(formset.as_table)
                    dt.status_order = formset['status_order']
                    dt.amount = formset['amount']
                    dt.price = formset['price']
                    dt.VAT = formset['VAT']
                    dt.save()
            except IntegrityError:
                print("Error encountered")
            
            return redirect('myprint:list')
    context['form'] = form
    context['formset'] = formset
    return render(request, 'multi_forms/create.html', context=context)








# def listview(request):
    
#     orders = OrderForm.objects.filter(manager=request.user.id).order_by('-id').first()
#     total = 0
#     all_price = orders.price * orders.amount
#     percent_sum = (all_price / 100) * orders.VAT
#     sum_list = all_price + percent_sum
#     total = total + sum_list
#     context = {}
#     context['orders'] = orders
#     context['sum_list'] = sum_list
#     context['all_price'] = all_price
#     context['total'] = total
#     if orders.VAT:
#         total = total + (total*orders.VAT/100)
#         context['total_sum']=total
        
#     return render(request, 'multi_forms/list.html', context=context)






@csrf_exempt
def user_login(request):
    if request.method == 'GET':
        print("GET ---------------> ")
        form = UserLoginForm()
        context={'form': form}
        print(context)
        return render(request, template_name='main/login.html', context=context)
    else:
        form = UserLoginForm(request.POST)
        
        if form.is_valid():
            
            user_name = request.POST['phone_number']
            password = request.POST['password']

            print("phone   ", user_name)
            print("password --> ", password)
            user = User.objects.filter(phone_number=user_name).first()

            user = authenticate(phone_number=user_name, password=password)
            print("user --- ", user)
            if user:    
                auth_login(request, user)
                print("login ---> ", auth_login)
                return  render(request, 'main/success.html')
            else:
                return render(request, template_name='main/error.html', context={'login': auth_login})





def pdf_report_create(request):
    order = OrderForm.objects.all()

    template_path = 'pdf_convert/pdfReport.html'

    context = {'order': order}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="orders_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response