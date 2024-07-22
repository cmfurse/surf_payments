from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from payments.models import User

admin.site.register(User, UserAdmin)
