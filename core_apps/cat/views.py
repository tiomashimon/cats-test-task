from django.shortcuts import render
from .serializers import CatSerializer
from .models import Cat
from rest_framework.viewsets import ModelViewSet
import requests
from rest_framework.response import Response

class CatViewSet(ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    lookup_field = 'pk'

