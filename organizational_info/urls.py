# organizational_info/urls.py
from django.urls import path
from . import views

app_name = 'organizational_info'

urlpatterns = [
    path('internal_control/', views.internal_control_list, name='internal_control_list'),
    path('internal_control/<int:pk>/', views.internal_control_detail, name='internal_control_detail'),
    path('internal_control/new/', views.internal_control_new, name='internal_control_new'),
    path('internal_control/<int:pk>/edit/', views.internal_control_edit, name='internal_control_edit'),
    path('internal_control/<int:pk>/delete/', views.internal_control_delete, name='internal_control_delete'),
    
    # Similar patterns for Corporate Governance and Accounting Process
]
