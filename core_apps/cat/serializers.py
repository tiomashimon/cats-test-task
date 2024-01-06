from rest_framework import serializers
from .models import Cat
import requests
from rest_framework.response import Response


class CatSerializer(serializers.ModelSerializer):
    url = serializers.CharField(read_only=True)
    cat_id = serializers.CharField(read_only=True)

    class Meta:
        model = Cat
        fields = '__all__'
    
    def create(self, validated_data):
        url = "https://api.thecatapi.com/v1/images/search?api_key=live_0ZaF7wzcIU1m1nBywb2T6jkZvbayDmsrbWADH2IsQkQWRnmkdHvYoTATgNoyuY9q"
        
        response = requests.get(url)
        json_data = response.json()
        
        cat_data = {
            'cat_id': json_data[0]['id'],
            'url': json_data[0]['url'],
        }

        return Cat.objects.create(**cat_data)