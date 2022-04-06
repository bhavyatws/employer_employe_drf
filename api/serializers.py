from distutils.errors import CompileError
from django.contrib.auth import get_user_model
User = get_user_model()
from api.models import Task,Comment,AssignedTask
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['id','username']

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password','employer']

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    comment = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [ 'id','task', 'task_deadline', 'user','comment']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Comment
        fields = ['comment','datetime','task','user' ]

class AssignedTaskToSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AssignedTask
        fields = ['assigned_to','task_assigned' ]

class GetAssignedTaskSerializer(serializers.ModelSerializer):
    task_assigned=serializers.StringRelatedField()
    class Meta:
        model = AssignedTask
        fields = ['task_assigned']
    # def task_assigned(self, obj):
       
    #    task_assigned = Task.objects.all()
    #    return GetAssignedTaskSerializer(task_assigned, many=True).data
    