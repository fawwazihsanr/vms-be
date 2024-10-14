from django.contrib import admin

from vms.visitor.models import Destination

class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Destination, DestinationAdmin)
# Register your models here.
