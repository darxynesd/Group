from django.shortcuts import render

# Create your views here.

def surveys_list(request):
    """Список опитувань"""
    return render(request, 'surveys/list.html')

def survey_detail(request, pk):
    """Детальна інформація про опитування"""
    return render(request, 'surveys/detail.html')

def take_survey(request, pk):
    """Пройти опитування"""
    return render(request, 'surveys/take.html')

def survey_results(request, pk):
    """Результати опитування"""
    return render(request, 'surveys/results.html')
