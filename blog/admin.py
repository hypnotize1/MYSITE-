from django.contrib import admin
from blog.models import post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

class postAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_views', 'status', 'login_require','published_date', 'created_date', 'author')
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

admin.site.register(post, postAdmin)

admin.site.register(Category)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'Post', 'approved', 'created_date',)
    list_filter = ('Post', 'approved')
    search_fields = ['name', 'Post']
    
admin.site.register(Comment, CommentAdmin)
