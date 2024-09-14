from random import choice, shuffle
from string import ascii_letters, digits

from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .emails import PasswordCreationEmail
from .models import CustomUser, ResetPasswordToken


class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label=_("password"))
    password_confirmation = forms.CharField(widget=forms.PasswordInput, label=_("password confirmation"))

    def clean_password(self):
        password = self.cleaned_data.get("password")
        try:
            # AUTH_PASSWORD_VALIDATORS in the settings are used.
            validate_password(password)
        except ValidationError as error:
            self.add_error('password', error)
        return password

    def clean_password_confirmation(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password_confirmation = self.cleaned_data.get("password_confirmation")
        if password and password_confirmation and password != password_confirmation:
            raise ValidationError(_("Les deux mots de passe ne sont pas identiques"))
        return password_confirmation
    

class PasswordSetFrom(PasswordForm):
    token = forms.CharField(widget=forms.HiddenInput) 

    def clean_token(self):
        # Check if the token exist.
        token = self.cleaned_data.get("token")
        token_obj = ResetPasswordToken.objects.filter(key=token).first()
        if not (token_obj and token_obj.is_valid()):
            raise ValidationError(_("Ce token n'est pas ou n'est plus attribué."))
        return token
    

class PasswordResetForm(forms.Form):
    email = forms.EmailField()


class UserCreationForm(forms.ModelForm, PasswordForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    class Meta:
        model = CustomUser
        fields = (
            'email', 'first_name', 'last_name',
            'is_active', 'is_staff', "is_superuser",
            'company'
        )

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
        return user
    

class AdminCreationUserForm(forms.ModelForm):
    """This form is used to create user with no specified password. This one \
    is generated randomly in the first place and a email is sent to the \
    user with an url and a token that allow him to chose his own password."""

    class Meta:
        model = CustomUser
        fields = (
            'email', 'first_name', 'last_name',
            'is_active', 'is_staff', "is_superuser",
            'company', 'password'
        )
        exclude = ["password"]

    @staticmethod
    def get_random_password():
        characters = [choice(digits) for i in range(10)]\
        + [choice(ascii_letters) for i in range(10)]\
        + ["!", "@", "$", "%","^", "&", "*", "+", "#"]
        shuffle(characters)
        return "".join(characters)

    def save(self, commit=True, *args, **kwargs):
        user = super().save(commit=False)
        user.set_password(self.get_random_password())
        if commit:
            user.save()
        token = ResetPasswordToken.objects.create(user=user)
        PasswordCreationEmail(user.email, token).send()
        return user
    