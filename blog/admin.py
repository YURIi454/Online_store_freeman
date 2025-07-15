from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','blog_owner', 'publication', 'watch_count')
    list_filter = ('name',)
    search_fields = ('name',)
