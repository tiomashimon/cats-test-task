import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from .models import Cat, CatVote
from .serializers import CatSerializer, CatVoteSerializer


class CatViewSet(ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    lookup_field = "pk"


class CatVoteViewSet(ModelViewSet):
    serializer_class = CatVoteSerializer

    def get_queryset(self):
        queryset = CatVote.objects.filter(vote=1, user=self.request.user)
        return queryset


