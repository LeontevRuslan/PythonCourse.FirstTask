# from rest_framework import generics
# from django.shortcuts import get_object_or_404
# from .models import Task, Project
# from .serializers import TaskSerializer, ProjectSerializer, User


# class ProjectListCreateView(generics.ListCreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

# class ProjectRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

# class TaskListCreateView(generics.ListCreateAPIView):
#     serializer_class = TaskSerializer

#     def get_queryset(self):
#         project_id = self.kwargs.get('project_id')
#         return Task.objects.filter(project_id=project_id)

#     def perform_create(self, serializer):
#         project_id = self.kwargs.get('project_id')
#         project = get_object_or_404(Project, id=project_id)

#         assigned_user_id = self.request.data.get('assigned_user_id')
#         assigned_user = get_object_or_404(User, id=assigned_user_id)

#         author_id = self.request.data.get('author')
#         author = get_object_or_404(User, id=author_id)
        
#         serializer.save(project_id=project, assigned_user_id=assigned_user, author=author)

# class TaskRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TaskSerializer
    
#     def get_queryset(self):
#         project_id = self.kwargs.get('project_id')
#         return Task.objects.filter(project_id=project_id)

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Project, Task
from .forms import ProjectForm, TaskForm


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'object_list'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project-list')

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project-list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object
        return context

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Task.objects.filter(project_id=project_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.get(id=self.kwargs['project_id'])
        return context
    
class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project_id
        return context

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'

    def get_success_url(self):
        return reverse_lazy('task-list',
                            kwargs={'project_id': self.kwargs['project_id']})

    def form_valid(self, form):
        form.instance.project_id = Project.objects.get(id=self.kwargs['project_id'])
        return super().form_valid(form)
    
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'

    def get_success_url(self):
        return reverse_lazy('task-list',
                            kwargs={'project_id': self.kwargs['project_id']})
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('task-list', kwargs={'project_id': self.kwargs['project_id']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.object
        context['project'] = self.object.project_id
        return context