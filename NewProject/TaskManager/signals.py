from django.core.mail import EmailMessage
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Task

def make_notification(email_address):
    email = EmailMessage(
        subject='You have been assigned a new task',  # Тема письма
        body='You have been assigned a new task. Please check your tasks list.',  # Тело письма
        to=[email_address],
    )
    email.send()

@receiver(pre_save, sender=Task)
def task_assignment_handler(instance, **kwargs):
    if instance.assigned_user_id:
        make_notification(instance.assigned_user_id.email)