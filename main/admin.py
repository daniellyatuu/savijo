from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'svg_icon', 'description_top_image', 'active', 'created_at', 'updated_at']

    search_fields = ['title']

admin.site.register(Service, ServiceAdmin)
