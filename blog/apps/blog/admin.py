from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'is_active')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
