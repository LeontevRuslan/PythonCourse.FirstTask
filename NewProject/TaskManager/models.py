from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid


User = get_user_model()


class BaseEntity(models.Model):
    id = models.CharField(max_length=40, unique=True, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            if not self.prefix:
                raise Exception('prefix required')
            self.id = f'{self.prefix}-{uuid.uuid4()}'
        super().save(*args, **kwargs)


class Project(BaseEntity):
    prefix = 'PRO'
    title = models.CharField(max_length=20)
    body = models.TextField()

    def __str__(self):
        return self.title



class Task(BaseEntity):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    prefix = 'TSK'
    title = models.CharField(max_length=20)
    body = models.TextField()
    deadline = models.DateTimeField(null = True)
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='todo'
    )
    assigned_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name = 'assigned'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name = 'author'
    )
    project_id = models.ForeignKey(
        Project, on_delete=models.CASCADE
    )

    def is_overdue(self):
        if self.deadline:
            return self.deadline < timezone.now()
        return False

    def __str__(self):
        return self.title
