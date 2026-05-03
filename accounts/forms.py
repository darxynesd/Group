from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логін")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    REGISTRATION_ROLE_CHOICES = (
        (Profile.ROLE_USER, "Користувач"),
        (Profile.ROLE_MODERATOR, "Модератор"),
        ("teacher", "Викладач"),
        ("project_lead", "Керівник проєкту"),
    )

    first_name = forms.CharField(label="Ім'я", max_length=150, required=True)
    last_name = forms.CharField(label="Прізвище", max_length=150, required=True)
    email = forms.EmailField(label="Email", required=True)
    requested_role = forms.ChoiceField(label="Роль", choices=REGISTRATION_ROLE_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email", "requested_role")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Користувач з таким email вже існує.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileDetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "phone")
