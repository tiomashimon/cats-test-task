from rest_framework.response import Response
from rest_framework import serializers
from .tasks import send_email_to_user
from ..user.models import User
from django.conf import settings
from .models import Verification
import random


class EmailVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def generate_verification_code(self):
        return random.randint(100000, 999999)

    def send_verification_email(self, email, verification_code, user):
        subject = 'Verification Code'
        message = f'Your verification code is: {verification_code}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        Verification.objects.create(email=email, code=verification_code,user=user)
        send_email_to_user.delay(subject, message, from_email, recipient_list)

    def validate(self, data):
        email = data['email']
        user= User.objects.filter(email=email).first()
        if user:
            verification_code = self.generate_verification_code()
            self.send_verification_email(email, verification_code, user)
            
            return data
        else:
            raise serializers.ValidationError('User with this email does not exist.')

    def verify_code(self, email, code):
        try:
            message = ''
            user = User.objects.filter(email=email).first()
            if not user:
                message = 'User credentials does not match!'
                return message
            verification = Verification.objects.filter(email=email, code=code).first()
            if verification.is_alive:
                if user.email_verificated:
                    message = 'User is already verificated!'
                    return message
                user.email_verificated = True
                user.save()
                message = 'Verification successful'
                return message
            else:
                message = 'Verification code expired!'
                return message
                
        except Verification.DoesNotExist:
            return False



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'email_verificated',
        )