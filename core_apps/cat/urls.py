from django.urls import path
from .views import CatViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', CatViewSet, basename='cat')

urlpatterns = [
] 

urlpatterns += router.urls
