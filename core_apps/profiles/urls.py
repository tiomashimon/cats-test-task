from django.urls import path
from .views import ProfileRetrieveAPIView


urlpatterns = [
    path('<int:pk>/', ProfileRetrieveAPIView.as_view(), name='profile'),
] 

