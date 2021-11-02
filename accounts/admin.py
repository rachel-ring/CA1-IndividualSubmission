from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import Profile


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff',]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)