from django.shortcuts import render

def domain_for_sale(request):
    return render(request, 'for_sale.html')