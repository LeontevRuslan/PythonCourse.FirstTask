from rest_framework import serializers
from .models import Task, Project

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'body',
                  'deadline', 'status',
                  'assigned_user_id', 'author',
                  'project_id']

    def update(self, instance, validated_data): 
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.status = validated_data.get('status', instance.status)
        instance.assigned_user_id = validated_data.get('assigned_user_id', instance.assigned_user_id)
        instance.author = validated_data.get('author', instance.author)
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.save()
        return instance


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'