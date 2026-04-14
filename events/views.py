from django.shortcuts import render

# Create your views here.

def events_list(request):
    """Список подій"""
    return render(request, 'events/list.html')

def calendar_view(request):
    """Календар подій"""
    return render(request, 'events/calendar.html')

def event_detail(request, pk):
    """Детальна інформація про подію"""
    return render(request, 'events/detail.html')
