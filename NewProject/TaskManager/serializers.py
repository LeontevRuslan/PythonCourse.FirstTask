from rest_framework import serializers
from .models import Task, Project, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    assigned_user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    project_id = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        
        assigned_user_id = validated_data.pop('assigned_user_id')
        author = validated_data.pop('author')
        project_id = validated_data.pop('project_id')

        task = Task.objects.create(
            assigned_user_id=assigned_user_id,
            author=author,
            project_id=project_id,
            **validated_data
        )
        return task