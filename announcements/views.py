from django.shortcuts import render

# Create your views here.

def announcements_list(request):
    """Список оголошень"""
    return render(request, 'announcements/list.html')

def announcement_detail(request, pk):
    """Детальна інформація про оголошення"""
    return render(request, 'announcements/detail.html')
