from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.forms import ModelForm
from django.http import Http404
from organizations.backends.forms import UserRegistrationForm
from organizations.models import OrganizationUser

from user.models import User


class UserSignupForm(ModelForm):
    class Meta:
        model = User
        fields = ("email", "password")

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "pa2 input-reset ba br2 bg-transparent w-100",
            }
        )
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "placeholder": "Password",
                "class": "pa2 input-reset ba br2 bg-transparent w-100",
            }
        )
    )


class OrganizationAcceptForm(ModelForm):
    """
    Form class for completing a user's registration and activating the
    User.
    The class operates on a user model which is assumed to have the required
    fields of a BaseUserModel
    """

    email = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "pa2 input-reset ba br2 bg-transparent w-100",
            }
        ),
    )
    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "pa2 input-reset ba br2 bg-transparent w-100",
            }
        ),
    )
    password_confirm = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password (confirmation)",
                "class": "pa2 input-reset ba br2 bg-transparent w-100",
            }
        ),
    )

    def clean(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password != password_confirm or not password:
            raise forms.ValidationError("Your password entries must match")
        return super(OrganizationAcceptForm, self).clean()

    class Meta:
        model = get_user_model()
        fields = ["email", "password"]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["name", "image", "show_information_tooltips"]

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "pa2 input-reset ba br2 bg-transparent w-100",
            }
        )
    )

    image = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "placeholder": "Profile Image",
                "class": "pa2 input-reset ba br2 bg-transparent w-100",
                "style": "box-sizing: border-box",
            }
        ),
    )
