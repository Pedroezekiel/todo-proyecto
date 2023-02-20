from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path("accounts/", include('rest_registration.api.urls')),
    path("login/", TokenObtainPairView.as_view(), name='token_obtain_pair')
]