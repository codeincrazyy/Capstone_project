from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from inventory.views import RegisterView
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponse("Welcome to the Inventory Management API!")),
    # Inventory app routes
    path('api/', include('inventory.urls')),  # /api/items/ and /api/changes/

    # Auth routes
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
