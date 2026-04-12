from django.urls import path
from .views import health_check, signup_preview

urlpatterns = [
    path("health/", health_check, name="health-check"),
    path("signup-preview/", signup_preview, name="signup-preview"),
]