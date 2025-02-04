from django.core.mail import EmailMessage
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Task, User

def make_notification(email_address):
    email = EmailMessage('You are get the task', to=['emai_address'])
    email.send()

@receiver(pre_save, sender=Task)
def handler(instance, **kwargs):
    if instance.assigned_user_id:
        make_notification(instance.assigned_user_id.email)