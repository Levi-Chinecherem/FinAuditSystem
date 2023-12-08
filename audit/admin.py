# audit/admin.py
from django.contrib import admin
from .models import AuditLog

class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_action_display', 'description', 'source_ip', 'related_object', 'timestamp')
    search_fields = ('user__username', 'action', 'related_object')
    list_filter = ('action', 'related_object', 'timestamp')

    def get_action_display(self, obj):
        return obj.get_action_display()
    get_action_display.short_description = 'Action'

# Customize the site header, title, and index title
admin.site.site_header = 'FinAuditSystem Administration'
admin.site.site_title = 'FinAuditSystem Admin Portal'
admin.site.index_title = 'Welcome to the FinAuditSystem Admin Portal'

# Register the model with the customized admin
admin.site.register(AuditLog, AuditLogAdmin)
