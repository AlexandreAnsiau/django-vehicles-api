from django.contrib import admin
from django.http import HttpRequest
from django.http.response import HttpResponse

from .forms import AdminCreationUserForm, UserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, *args, **kwargs):
        if not obj:
            kwargs["form"] = UserCreationForm
        return super().get_form(request, obj, *args, **kwargs)
    
