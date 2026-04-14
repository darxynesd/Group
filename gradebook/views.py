from django.shortcuts import render

# Create your views here.

def gradebook_index(request):
    """Електронний щоденник"""
    return render(request, 'gradebook/index.html')

def student_grades(request, pk):
    """Оцінки студента"""
    return render(request, 'gradebook/student_grades.html')
