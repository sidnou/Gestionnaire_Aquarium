from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomManager,CustomUser
# Register your models here.
@admin.register(CustomUser,UserAdmin)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = "__all__"
