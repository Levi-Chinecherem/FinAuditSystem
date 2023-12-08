from django.urls import path
from . import views

app_name = 'audit'

urlpatterns = [
    path('audit-logs/', views.audit_log_list, name='audit_log_list'),
    path('audit-log/<int:audit_log_id>/', views.audit_log_detail, name='audit_log_detail'),
    path('create/', views.audit_log_create, name='audit_log_create'),
    path('edit/<int:audit_log_id>/', views.audit_log_update, name='audit_log_update'),
    path('delete/<int:audit_log_id>/', views.audit_log_delete, name='audit_log_delete'),
]
