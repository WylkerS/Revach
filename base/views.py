from django.shortcuts import render

def home_page(request):
    return render(request, 'pages/home_page.html')

def transactions_page(request):
    return render(request, 'pages/transactions_page.html')

def categories_page(request):
    return render(request, 'pages/categories_page.html')