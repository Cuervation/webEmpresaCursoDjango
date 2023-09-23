from django.contrib import admin
from .models import Service
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fiels = ('created','updated')

admin.site.register(Service,ServiceAdmin)    