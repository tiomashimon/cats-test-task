from rest_framework.response import Response
from rest_framework import serializers
from django.core.mail import send_mail
from ..user.models import User
from django.conf import settings
from .models import Verification
import random


class EmailVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def generate_verification_code(self):
        return random.randint(100000, 999999)

    def send_verification_email(self, email, verification_code):
        subject = 'Verification Code'
        message = f'Your verification code is: {verification_code}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

    def validate(self, data):
        email = data['email']
        user_exists = User.objects.filter(email=email).exists()
        if user_exists:
            verification_code = self.generate_verification_code()
            self.send_verification_email(email, verification_code)
            
            return data
        else:
            raise serializers.ValidationError('User with this email does not exist.')

    def verify_code(self, email, code):
        try:
            message = ''
            user = User.objects.get(email=email)
            if user.email_verificated:
                message = 'User is already verificated!'
                return message
            user.email_verificated = True
            user.save()
            message = 'Verification successful'
            return True
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