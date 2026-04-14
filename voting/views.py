from django.shortcuts import render

# Create your views here.

def voting_list(request):
    """Список голосувань"""
    return render(request, 'voting/list.html')

def voting_detail(request, pk):
    """Детальна інформація про голосування"""
    return render(request, 'voting/detail.html')

def cast_vote(request, pk):
    """Проголосувати"""
    return render(request, 'voting/cast_vote.html')

def voting_results(request, pk):
    """Результати голосування"""
    return render(request, 'voting/results.html')
