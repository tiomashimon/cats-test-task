from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CatViewSet, CatVoteViewSet

router = DefaultRouter()
router.register("vote", CatVoteViewSet, basename="cat_vote")
router.register("", CatViewSet, basename="cat")

urlpatterns = []

urlpatterns += router.urls
