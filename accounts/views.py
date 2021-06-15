from django.shortcuts import render
# from django.http import HttpResponse
from .models import *



# Create your views here.

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    

    # total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()


    context = {'customers' : customers,'orders': orders,
    #  'total_customers': total_customers,
      'total_orders': total_orders,
       'delivered': delivered, 'pending': pending
    }

    return render(request, "accounts/dashboard.html", context)

def products(request):
    products = Product.objects.all()
    return render(request, "accounts/products.html", {'products': products},)

def customer(request):
    return render(request, "accounts/customer.html")
