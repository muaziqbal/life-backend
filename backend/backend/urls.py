from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh
    path('api/auth/', include('auth_service.urls')),  # include your app’s routes
    path('api/user/', include('user_service.urls')),  # include user service routes
    path('api/roles/', include('role_service.urls')),
    path('api/learner/', include('learner_service.urls')),
]
