# risk_assessment/urls.py
from django.urls import path
from .views import (
    risk_assessment_list,
    risk_assessment_detail,
    risk_assessment_create,
    risk_assessment_update,
    risk_assessment_delete,
)

app_name = 'risk_assessment'

urlpatterns = [
    path('', risk_assessment_list, name='risk_assessment_list'),
    path('<int:pk>/', risk_assessment_detail, name='risk_assessment_detail'),
    path('create/', risk_assessment_create, name='risk_assessment_create'),
    path('<int:pk>/update/', risk_assessment_update, name='risk_assessment_update'),
    path('<int:pk>/delete/', risk_assessment_delete, name='risk_assessment_delete'),
]
