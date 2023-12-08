# risk_assessment/admin.py
from django.contrib import admin
from .models import RiskAssessment

class RiskAssessmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'description', 'impact', 'likelihood', 'timestamp')
    list_filter = ('category', 'timestamp')
    search_fields = ('user__username', 'category', 'timestamp')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)

admin.site.register(RiskAssessment, RiskAssessmentAdmin)
