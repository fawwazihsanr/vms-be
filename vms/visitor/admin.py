from django.contrib import admin

from vms.visitor.models import Destination, Visitor


class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Destination, DestinationAdmin)
# Register your models here.

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_card', 'vendor', 'check_in_date', 'check_out_date', 'created_by', 'status')
    search_fields = ('name', 'id_card', 'vendor', 'company', 'person_to_visit_name')
    list_filter = ('status', 'company', 'vendor', 'check_in_date', 'check_out_date')
    readonly_fields = ('created', 'modified')
admin.site.register(Visitor, VisitorAdmin)
