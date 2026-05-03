from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse

from accounts.models import Profile
from accounts.services import get_role_label, get_user_role


def index(request):
    widgets = [
        {
            "title": "Форум групи",
            "description": "Обговорення питань, ідей і організаційних рішень.",
            "url": reverse("forum:index"),
            "link_text": "Перейти до форуму",
        },
        {
            "title": "Щоденник",
            "description": "Оперативний доступ до оцінок і навчального прогресу.",
            "url": reverse("gradebook:index"),
            "link_text": "Відкрити щоденник",
        },
        {
            "title": "Події",
            "description": "Календар пар, зустрічей, дедлайнів та активностей.",
            "url": reverse("events:list"),
            "link_text": "Переглянути події",
        },
        {
            "title": "Оголошення",
            "description": "Важливі повідомлення від модераторів та адміністраторів.",
            "url": reverse("announcements:list"),
            "link_text": "Перейти до оголошень",
        },
        {
            "title": "Матеріали",
            "description": "Файли, посилання та допоміжні ресурси для навчання.",
            "url": reverse("materials:list"),
            "link_text": "Відкрити матеріали",
        },
        {
            "title": "Галерея",
            "description": "Фото і відео з подій та командних активностей.",
            "url": reverse("gallery:list"),
            "link_text": "Перейти до галереї",
        },
    ]

    total_users = User.objects.count()
    moderators = Profile.objects.filter(role=Profile.ROLE_MODERATOR).count()
    admins = User.objects.filter(is_superuser=True).count()
    admins += Profile.objects.filter(role=Profile.ROLE_ADMIN, user__is_superuser=False).count()

    current_role = get_user_role(request.user) if request.user.is_authenticated else ""

    context = {
        "group_name": "Портал академічної групи",
        "group_description": "Єдина точка доступу до комунікації, матеріалів і командної взаємодії.",
        "widgets": widgets,
        "total_users": total_users,
        "moderators": moderators,
        "admins": admins,
        "current_role_label": get_role_label(current_role) if current_role else "Гість",
    }
    return render(request, "home/index.html", context)
