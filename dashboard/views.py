from django.shortcuts import render
from rest import *

# Create your views here.


def dashboard(request):
    products = get_all('products').json();
    workstations = get_all('workstations').json();
    pareto_error = get_all('reasons').json();
    context = {
        'products': products,
        'workstations': workstations,
        'pareto_error': pareto_error
    }
    return render(request, 'dashboard.html',context)