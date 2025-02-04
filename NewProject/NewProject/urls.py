# from django.urls import path
# from TaskManager.views import tasks, ProjectsView, ProjectRetrieveUpdateDestroyAPIView

# urlpatterns = [
#     path('tasks/', tasks, name='tasks'),
#     path('projects/', ProjectsView.as_view(), name='projects'),
#     path('tasks/<str:task_id>/', tasks, name='task_detail'),
#     path('projects/<str:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail')
# ]


# create project POST localhost:8000/project
# get project GET localhost:8000/project/:id
# create task get project POST localhost:8000/project/:id/tasks
# get task from project GET localhost:8000/project/:id/tasks

# urlpatterns = [
#     path('projects/<int:project_id>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
#     path('tasks/<int:pk>/', TaskRetrieveUpdateView.as_view(), name='task-detail'),
#     path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
# ]

from django.urls import path
from TaskManager.views import (
    ProjectListCreateView,
    ProjectRetrieveUpdateView,
    TaskListCreateView,
    TaskRetrieveUpdateView,
)

urlpatterns = [
    # GET /projects/ и POST /projects/
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),

    # GET /projects/:project_id/
    path('projects/<str:pk>/', ProjectRetrieveUpdateView.as_view(), name='project-detail'),

    # GET /projects/:project_id/tasks/ и POST /projects/:project_id/tasks/
    path('projects/<str:project_id>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),

    # GET /projects/:project_id/tasks/:task_id/
    path('projects/<str:project_id>/tasks/<str:pk>/', TaskRetrieveUpdateView.as_view(), name='task-detail'),
]