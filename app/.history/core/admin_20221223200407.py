from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin



@admin.register(Usuario)
@admin.register(Productos)