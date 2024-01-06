from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .models import Profile
from .serializers import ProfileSerializer


class ProfileRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()