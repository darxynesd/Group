from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import LoginForm, ProfileDetailsForm, ProfileUserForm, RegistrationForm
from .models import Profile
from .services import (
    get_or_create_profile,
    get_role_label,
    get_user_role,
    resolve_registration_role,
    set_user_role,
)


def get_safe_next_url(request):
    candidate = request.POST.get("next") or request.GET.get("next")
    if candidate and url_has_allowed_host_and_scheme(
        candidate,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return candidate
    return ""


def user_login(request):
    if request.user.is_authenticated:
        return redirect("accounts:profile")

    next_url = get_safe_next_url(request)
    form = LoginForm(request=request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        get_or_create_profile(user)
        return redirect(next_url or "home:index")

    return render(request, "home/login.html", {"form": form, "next": next_url})


def user_logout(request):
    logout(request)
    return redirect("home:index")


def register(request):
    if request.user.is_authenticated:
        return redirect("accounts:profile")

    form = RegistrationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        role = resolve_registration_role(form.cleaned_data["requested_role"])
        set_user_role(user, role)
        login(request, user)
        return redirect("accounts:profile")

    return render(request, "home/register.html", {"form": form})


@login_required
def profile(request):
    profile_obj = get_or_create_profile(request.user)
    user_form = ProfileUserForm(request.POST or None, instance=request.user)
    profile_form = ProfileDetailsForm(request.POST or None, instance=profile_obj)

    if request.method == "POST" and user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        return redirect("accounts:profile")

    current_role = get_user_role(request.user)
    can_access_admin = current_role == Profile.ROLE_ADMIN or request.user.is_superuser

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "current_role": current_role,
        "current_role_label": get_role_label(current_role),
        "can_access_admin": can_access_admin,
    }
    return render(request, "home/profile.html", context)
