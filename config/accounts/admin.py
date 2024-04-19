from django.contrib import admin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email','username',]


admin.site.register(CustomUser,CustomUserAdmin)