from django import forms
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'body']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'body', 'deadline', 'status',
                  'assigned_user_id', 'author', 'project_id']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }