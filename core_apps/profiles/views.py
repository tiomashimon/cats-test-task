from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated


from rest_framework.permissions import BasePermission


class ProfileAPIView(APIView):
    permission_classes =[IsAuthenticated]
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        try:
            user = request.user
            profile = Profile.objects.get(user=user)
            if request.user == profile.user:
                serializer = ProfileSerializer(profile)
                return Response(serializer.data)
            return Response({'Succes':False}, status= status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            return Response(
                {"error": f"Profile with user={user} does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def put(self, request, *args, **kwargs):
        try:
            user = request.user
            profile = Profile.objects.get(user=user)
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            return Response(
                {"error": f"Profile with pk={pk} does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
