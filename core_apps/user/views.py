from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import EmailVerificationSerializer


class EmailVerificationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = EmailVerificationSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                {'message': 'Verification code sent successfully'},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        verification_code = request.data.get('verification_code', '')

        serializer = EmailVerificationSerializer()
        message = serializer.verify_code(email, verification_code)
        if message:
            return Response({'message': message}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'message': 'Verification code does not match'},
                status=status.HTTP_400_BAD_REQUEST,
            )
