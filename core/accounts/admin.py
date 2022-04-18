from django.contrib import admin

from .models import User
from django.utils.html import mark_safe
# Register your models here
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email','image_tag','id']

    def image_tag(self,obj):
        return mark_safe(f'<img src="/media/{obj.image}" width="100" height="100"/>')