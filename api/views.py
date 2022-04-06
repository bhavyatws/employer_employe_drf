
from django.contrib.auth import get_user_model


User=get_user_model()
from .serializers import RegisterSerializer,TaskSerializer,CommentSerializer,AssignedTaskToSerializer,UserSerializer,GetAssignedTaskSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_class=[IsAuthenticated]
    permission_classes=[IsAuthenticated]





from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from api.permissions import IsOwnerOrReadOnly,IsEmployer


from rest_framework import viewsets

from api.models import Task,Comment,AssignedTask



class AddTask(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[IsAuthenticated,IsEmployer]
    authentication_class=[IsAuthenticated]
    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)



class Comment(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)


     
class CreateAssignedTaskTo(generics.CreateAPIView):
    queryset = AssignedTask.objects.all()
    serializer_class = AssignedTaskToSerializer
    permission_classes = [IsAuthenticated,IsEmployer]
    authentication_class = [IsAuthenticated]

class ListAssignedTaskTo(generics.ListAPIView):
    def get_queryset(self):
        return AssignedTask.objects.filter(assigned_to=self.request.user)
        
    serializer_class = AssignedTaskToSerializer
    permission_classes = [IsAuthenticated]
    authentication_class = [IsAuthenticated]
    


from .models import Comment as CommentModel
class GetList(generics.ListAPIView):

    def get_queryset(self):
        id=self.request.GET.get('id')
        print("id",id)
        task=Task.objects.get(id=id)
        print(task)
        comment=CommentModel.objects.filter(task=task)
        return comment

    serializer_class = CommentSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

   

class GetAssignedList(generics.ListAPIView):
    
    queryset=AssignedTask.objects.all()
    serializer_class =GetAssignedTaskSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)
