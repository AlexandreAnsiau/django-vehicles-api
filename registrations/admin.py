from django.contrib import admin

from .forms import UserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    form = UserCreationForm