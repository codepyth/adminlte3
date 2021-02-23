from django.contrib import admin
from .models import Conference
# Register your models here.

# admin.site.register(conference)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue', 'details', 'city', 'state')
admin.site.register(Conference, AuthorAdmin)