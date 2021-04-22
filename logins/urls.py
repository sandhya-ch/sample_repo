from django.urls import path
from .views import RegisterAPI, LoginView

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')
]