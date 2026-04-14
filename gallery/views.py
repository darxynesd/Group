from django.shortcuts import render

# Create your views here.

def gallery_list(request):
    """Галерея"""
    return render(request, 'gallery/list.html')

def gallery_item_detail(request, pk):
    """Детальна інформація про елемент галереї"""
    return render(request, 'gallery/detail.html')
