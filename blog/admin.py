from django.contrib import admin

from .models import Blog, Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'blog_owner', 'publication', 'watch_count')
    list_filter = ('name',)
    search_fields = ('name',)
