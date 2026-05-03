from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile
from .services import set_user_role


class AccountsFlowTests(TestCase):
    def test_register_user_creates_profile_with_user_role(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "newuser",
                "first_name": "Ira",
                "last_name": "Bondar",
                "email": "newuser@example.com",
                "requested_role": Profile.ROLE_USER,
                "password1": "StrongPass12345!",
                "password2": "StrongPass12345!",
            },
        )

        self.assertRedirects(response, reverse("accounts:profile"))
        user = User.objects.get(username="newuser")
        self.assertTrue(user.groups.filter(name="Users").exists())
        self.assertEqual(user.profile.role, Profile.ROLE_USER)
        self.assertFalse(user.is_staff)

    def test_register_teacher_sets_admin_role(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "teacher1",
                "first_name": "Olha",
                "last_name": "Koval",
                "email": "teacher1@example.com",
                "requested_role": "teacher",
                "password1": "StrongPass12345!",
                "password2": "StrongPass12345!",
            },
        )

        self.assertRedirects(response, reverse("accounts:profile"))
        user = User.objects.get(username="teacher1")
        self.assertEqual(user.profile.role, Profile.ROLE_ADMIN)
        self.assertTrue(user.groups.filter(name="Administrators").exists())
        self.assertTrue(user.is_staff)

    def test_login_flow(self):
        user = User.objects.create_user(
            username="loginuser",
            email="loginuser@example.com",
            password="StrongPass12345!",
        )
        set_user_role(user, Profile.ROLE_MODERATOR)

        response = self.client.post(
            reverse("accounts:login"),
            {"username": "loginuser", "password": "StrongPass12345!"},
        )

        self.assertRedirects(response, reverse("home:index"))
        self.assertIn("_auth_user_id", self.client.session)

    def test_profile_update(self):
        user = User.objects.create_user(
            username="profileuser",
            email="profileuser@example.com",
            password="StrongPass12345!",
            first_name="Old",
            last_name="Name",
        )
        set_user_role(user, Profile.ROLE_USER)
        self.client.force_login(user)

        response = self.client.post(
            reverse("accounts:profile"),
            {
                "first_name": "New",
                "last_name": "Surname",
                "email": "profileuser_new@example.com",
                "bio": "Student profile",
                "phone": "+380501112233",
            },
        )

        self.assertRedirects(response, reverse("accounts:profile"))
        user.refresh_from_db()
        self.assertEqual(user.first_name, "New")
        self.assertEqual(user.last_name, "Surname")
        self.assertEqual(user.email, "profileuser_new@example.com")
        self.assertEqual(user.profile.bio, "Student profile")
        self.assertEqual(user.profile.phone, "+380501112233")
