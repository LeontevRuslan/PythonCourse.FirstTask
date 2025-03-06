# from django.contrib import admin
# from django.urls import path
# from TaskManager.views import (
#     ProjectListCreateView,
#     ProjectRetrieveUpdateView,
#     TaskListCreateView,
#     TaskRetrieveUpdateView,
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # GET /projects/ и POST /projects/
#     path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),

#     # GET /projects/:project_id/
#     path('projects/<str:pk>/', ProjectRetrieveUpdateView.as_view(), name='project-detail'),

#     # GET /projects/:project_id/tasks/ и POST /projects/:project_id/tasks/
#     path('projects/<str:project_id>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),

#     # GET /projects/:project_id/tasks/:task_id/
#     path('projects/<str:project_id>/tasks/<str:pk>/', TaskRetrieveUpdateView.as_view(), name='task-detail'),
# ]


from django.urls import path
from TaskManager.views import (
    ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView,
    TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
)

urlpatterns = [
    # Проекты
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<str:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('projects/<str:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<str:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),

    # Задачи
    path('projects/<str:project_id>/tasks/', TaskListView.as_view(), name='task-list'),
    path('projects/<str:project_id>/tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('projects/<str:project_id>/tasks/<str:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('projects/<str:project_id>/tasks/<str:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('projects/<str:project_id>/tasks/<str:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]