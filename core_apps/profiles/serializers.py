from rest_framework import serializers
from ..user.serializers import UserSerializer

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = "__all__"
