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
        #by writing extra_kwargs ,now password will be only be shown during registration
        extra_kwargs={'password':{'write_only':True,'min_length':5}}



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Comment
        fields = ['comment','datetime','task','user' ]

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [ 'id','task', 'task_deadline', 'user','comment']
    def create(self, validated_data):
        comment_data = validated_data.pop('comment')
        task= Task.objects.create(**validated_data)
        for comment in task:
            Comment.objects.create(task=task, **comment_data)
        return task

class AssignedTaskToSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AssignedTask
        fields = ['assigned_to','task_assigned' ]

class GetAssignedTaskSerializer(serializers.ModelSerializer):
    task_assigned=TaskSerializer()
    class Meta:
        model = AssignedTask
        fields = ['task_assigned']

    def create(self, validated_data):
        task_assigned = validated_data.pop('task_assigned')
        assigned_task= AssignedTask.objects.create(**validated_data)
        for task in task_assigned:
            Task.objects.create(task=assigned_task, **task_assigned)
        return assigned_task
    # def task_assigned(self, obj):
       
    #    task_assigned = Task.objects.all()
    #    return GetAssignedTaskSerializer(task_assigned, many=True).data
    