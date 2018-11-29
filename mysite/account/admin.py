from django.contrib import admin
from .models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'phone')
    list_filter = ('phone',) #定义右边栏显示的过滤器的内容

admin.site.register(UserProfile, UserProfileAdmin)