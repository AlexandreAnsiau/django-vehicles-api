from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    class Meta:
        model = CustomUser
        fields = (
            'email', 'first_name', 'last_name',
            'is_active', 'is_staff', "is_superuser",
            'company', 'password'
        )
        widgets = {
            "password": forms.PasswordInput
        }

    password_confirmation = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data.get("password")
        try:
            # AUTH_PASSWORD_VALIDATORS in the settings are used.
            validate_password(self.cleaned_data.get("password"))
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

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
        return user