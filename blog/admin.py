from django.contrib import admin
from blog.models import post, Category


class postAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_views', 'status', 'published_date', 'created_date', 'author')
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']

admin.site.register(post, postAdmin)

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    pass