from django.contrib import admin
from .models import Profile
admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','profile_pic','bio']
    raw_id_fields = ['user']
# Register your models here.
