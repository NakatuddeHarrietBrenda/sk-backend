from django.contrib import admin
from django.urls import path, include
from dashboard.views import admin_dashboard
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
    path("api/properties/", include("properties.urls")),
    path("api/payments/", include("payments.urls")),
    path("api/contact/", include("contacts.urls")),
    path("api/dashboard/", include("dashboard.urls")),
    path('admin/dashboard/', include('dashboard.urls')),
    path("api/users/", include("users.urls")),

    path('admin/', admin.site.urls),
   
    path('dashboard/', admin_dashboard, name='dashboard'),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)