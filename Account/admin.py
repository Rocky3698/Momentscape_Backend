from django.contrib import admin
from .models import UserAddress, UserProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserAddress)