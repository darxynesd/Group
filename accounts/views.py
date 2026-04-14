from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

# Create your views here.

def user_login(request):
    """Вхід користувача"""
    return render(request, 'accounts/login.html')

def user_logout(request):
    """Вихід користувача"""
    logout(request)
    return redirect('home:index')

def register(request):
    """Реєстрація нового користувача"""
    return render(request, 'accounts/register.html')

def profile(request):
    """Профіль користувача"""
    return render(request, 'accounts/profile.html')
