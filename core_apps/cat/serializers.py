import requests
from rest_framework import serializers
from rest_framework.response import Response

from .models import Cat, CatVote
from ..user.models import User
from ..user.serializers import UserSerializer


class CatSerializer(serializers.ModelSerializer):
    url = serializers.CharField(read_only=True)
    cat_id = serializers.CharField(read_only=True)
    width = serializers.IntegerField(read_only=True)
    height = serializers.IntegerField(read_only=True)
    

    class Meta:
        model = Cat
        fields = "__all__"

    def create(self, validated_data):
        url = "https://api.thecatapi.com/v1/images/search?api_key=live_0ZaF7wzcIU1m1nBywb2T6jkZvbayDmsrbWADH2IsQkQWRnmkdHvYoTATgNoyuY9q"

        response = requests.get(url)
        json_data = response.json()

        cat_data = {
            "cat_id": json_data[0]["id"],
            "url": json_data[0]["url"],
            "width": json_data[0]["width"],
            "height": json_data[0]["height"],
        }

        return Cat.objects.create(**cat_data)

class CatVoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    
    class Meta:
        model = CatVote
        fields = ('__all__')
    
    def create(self, validated_data):
        user = User.objects.get(username=validated_data.get("user"))
        if validated_data.get('vote') == 1:
            user.likes += 1
        else:
            user.dislikes += 1
        user.save()
        
        return CatVote.objects.create(**validated_data)

    
    