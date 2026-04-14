from django.shortcuts import render

# Create your views here.

def forum_index(request):
    """Головна сторінка форуму"""
    return render(request, 'forum/index.html')

def thread_detail(request, pk):
    """Детальна інформація про гілку форуму"""
    return render(request, 'forum/thread_detail.html')
