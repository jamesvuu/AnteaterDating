from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import UCIUser

# Register your models here.
admin.site.register(UCIUser, UserAdmin)
