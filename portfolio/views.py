from django.shortcuts import render

# Create your views here.

def portfolio_list(request):
    """Список портфоліо"""
    return render(request, 'portfolio/list.html')

def portfolio_detail(request, pk):
    """Детальна інформація про портфоліо"""
    return render(request, 'portfolio/detail.html')

def my_portfolio(request):
    """Моє портфоліо"""
    return render(request, 'portfolio/my.html')
