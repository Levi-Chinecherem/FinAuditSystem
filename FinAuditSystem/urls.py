from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Include core app URLs
    path('accounts/', include('accounts.urls')),  # Include accounts app URLs
    path('audit/', include('audit.urls')),  # Include audit app URLs
    path('organizational_info/', include('organizational_info.urls')),  # Include organizational_info app URLs
    path('risk_assessment/', include('risk_assessment.urls')),  # Include risk_assessment app URLs
]
