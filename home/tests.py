from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from accounts.models import Profile
from accounts.services import set_user_role


class HomePageTests(TestCase):
    def test_home_page_for_guest(self):
        response = self.client.get(reverse("home:index"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["current_role_label"], "Гість")
        self.assertEqual(len(response.context["widgets"]), 6)

    def test_home_page_role_statistics(self):
        user = User.objects.create_user(username="user1", password="StrongPass12345!")
        moderator = User.objects.create_user(username="mod1", password="StrongPass12345!")
        admin = User.objects.create_user(username="admin1", password="StrongPass12345!")

        set_user_role(user, Profile.ROLE_USER)
        set_user_role(moderator, Profile.ROLE_MODERATOR)
        set_user_role(admin, Profile.ROLE_ADMIN)

        response = self.client.get(reverse("home:index"))

        self.assertEqual(response.context["total_users"], 3)
        self.assertEqual(response.context["moderators"], 1)
        self.assertEqual(response.context["admins"], 1)
