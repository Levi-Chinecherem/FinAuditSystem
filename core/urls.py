from django.urls import path
from .views import index, dashboard

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    # Add more paths for other views if needed
]
