from django.contrib import admin
from website.models import Contact, newsletter

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ('name', 'message')
    date_hierarchy = 'created_date'

admin.site.register(Contact, ContactAdmin)
admin.site.register(newsletter)