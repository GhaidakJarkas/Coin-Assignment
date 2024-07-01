from django.urls import path
from coins.api import views


urlpatterns = [
    path('v1/coins/', views.coins, name='coins'),
]