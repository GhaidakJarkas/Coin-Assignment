from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from . import views




urlpatterns = [
    path('v1/register/', views.register, name='register'),
    path('v1/login/', views.log_in, name='login'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
]