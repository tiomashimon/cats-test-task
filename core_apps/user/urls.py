from django.urls import path

from .views import EmailVerificationAPIView

urlpatterns = [
    path('email/', EmailVerificationAPIView.as_view(), name='email'),
]
