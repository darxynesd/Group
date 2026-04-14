from django.shortcuts import render

# Create your views here.

def materials_list(request):
    """Список матеріалів"""
    return render(request, 'materials/list.html')

def material_detail(request, pk):
    """Детальна інформація про матеріал"""
    return render(request, 'materials/detail.html')
