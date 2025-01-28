from django.urls import path
from TaskManager.views import tasks, projects

urlpatterns = [
    path('tasks/', tasks, name='tasks'),
    path('projects/', projects, name='projects'),
    path('tasks/<str:task_id>/', tasks, name='task_detail'),
]


# create project POST localhost:8000/project
# get project GET localhost:8000/project/:id
# create task get project POST localhost:8000/project/:id/tasks
# get task from project GET localhost:8000/project/:id/tasks