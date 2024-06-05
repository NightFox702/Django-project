# admin.py
from django.contrib import admin
from .models import SocialLink,Post

class SocialLinkInline(admin.TabularInline):
    model = SocialLink

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    search_fields = ['name', 'url']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
