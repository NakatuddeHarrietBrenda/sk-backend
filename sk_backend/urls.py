from django.contrib import admin
from django.urls import path, include
from core.views import admin_dashboard

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
    path("api/properties/", include("properties.urls")),
    path("api/payments/", include("payments.urls")),
    path("api/contact/", include("contacts.urls")),
    path("api/dashboard/", include("dashboard.urls")),

    path('admin/', admin.site.urls),
    path("api/", include("payments.urls")),
    path('api/', include('payments.urls')), 
    
    path('dashboard/', admin_dashboard, name='dashboard'),
        path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
]