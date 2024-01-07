from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer

class ProfileAPIView(APIView):
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            profile = Profile.objects.get(pk=pk)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response({"error": f"Profile with pk={pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request,*args, **kwargs):
        try:
            pk = kwargs.get('pk')
            profile = Profile.objects.get(pk=pk)
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            return Response({"error": f"Profile with pk={pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)
 