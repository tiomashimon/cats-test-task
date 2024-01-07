from main.celery import app
from datetime import timedelta
from django.utils import timezone
from .models import Verification
from django.core.mail import send_mail


@app.task
def delete_expired_codes():
    now = timezone.now()

    alive_verifications = Verification.objects.filter(is_alive=True)

    for code in alive_verifications:
        expiration_time = code.created_at + timedelta(minutes=5)
        if now >= expiration_time:
            print('Delete code: ' + code.email)
            code.is_alive = False
            code.save()

@app.task
def send_email_to_user(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)

