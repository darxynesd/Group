from django.contrib.auth.models import Group
from django.db import transaction

from .models import Profile


ROLE_TO_GROUP = {
    Profile.ROLE_USER: "Users",
    Profile.ROLE_MODERATOR: "Moderators",
    Profile.ROLE_ADMIN: "Administrators",
}


def ensure_role_groups():
    for group_name in ROLE_TO_GROUP.values():
        Group.objects.get_or_create(name=group_name)


def normalize_role(requested_role):
    if requested_role in dict(Profile.ROLE_CHOICES):
        return requested_role
    return Profile.ROLE_USER


def resolve_registration_role(requested_role):
    if requested_role == Profile.ROLE_MODERATOR:
        return Profile.ROLE_MODERATOR
    if requested_role in {"teacher", "project_lead"}:
        return Profile.ROLE_ADMIN
    return Profile.ROLE_USER


def get_or_create_profile(user):
    profile, _ = Profile.objects.get_or_create(user=user)
    if user.is_superuser and profile.role != Profile.ROLE_ADMIN:
        profile.role = Profile.ROLE_ADMIN
        profile.save(update_fields=["role", "updated_at"])
    return profile


@transaction.atomic
def set_user_role(user, requested_role):
    role = normalize_role(requested_role)
    ensure_role_groups()
    profile = get_or_create_profile(user)
    profile.role = role
    profile.save(update_fields=["role", "updated_at"])

    managed_groups = list(Group.objects.filter(name__in=ROLE_TO_GROUP.values()))
    if managed_groups:
        user.groups.remove(*managed_groups)
    user.groups.add(Group.objects.get(name=ROLE_TO_GROUP[role]))

    is_staff_required = role == Profile.ROLE_ADMIN or user.is_superuser
    if user.is_staff != is_staff_required:
        user.is_staff = is_staff_required
        user.save(update_fields=["is_staff"])

    return profile


def get_user_role(user):
    if not user.is_authenticated:
        return ""
    if user.is_superuser:
        return Profile.ROLE_ADMIN
    profile = get_or_create_profile(user)
    return profile.role


def get_role_label(role):
    return dict(Profile.ROLE_CHOICES).get(role, "Користувач")
