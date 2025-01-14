from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Project(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()


class Task(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    deadline = models.DateTimeField(null = True)
    status = models.CharField(max_length=20)
    assigned_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name = 'assigned'
    )
    author_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name = 'author'
    )
    project_id = models.ForeignKey(
        Project, on_delete=models.CASCADE
    )