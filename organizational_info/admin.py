# organizational_info/admin.py
from django.contrib import admin
from .models import InternalControl, CorporateGovernance, AccountingProcess

class InternalControlAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

# Register the models with the customized admins
admin.site.register(InternalControl, InternalControlAdmin)
