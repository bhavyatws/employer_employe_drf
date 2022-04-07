





from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager,PermissionsMixin,AbstractBaseUser

from django.utils.timezone import now
from .manager import CustomUserManager

# Create your models here.
#Create your customuser model here


#Create your user model here

class User(AbstractBaseUser,PermissionsMixin):
    #AbstractBaseUser has password,last_login,is_active by default
    username=models.CharField(db_index=True,max_length=50,unique=True)
    email=models.EmailField(db_index=True,unique=True,max_length=254,null=True,blank=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    date_joined=models.DateTimeField(default=now)
    employer=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)#must need,otherwise you will not able to login
    is_active=models.BooleanField(default=True)#must need,otherwise you will not able to login
    is_superuser=models.BooleanField(default=False)#This is inherited Permissions
    objects=CustomUserManager()
    # EMAIL_FIELD='email'
    USERNAME_FIELD='username'
    REQUIRED_FIELD = []
    class Meta:
        verbose_name='user'
        verbose_name_plural='users'
    def __str__(self):
        return self.username
   
from django.contrib.auth import get_user_model
User = get_user_model()

class Task(models.Model):
 
    task=models.CharField(max_length=250,default="")
    task_date=models.DateTimeField(auto_now=True)
    task_deadline=models.DateTimeField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.task + " - " + " " + str(self.task_deadline)


class Comment(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="user")
    comment=models.TextField(default='')
    datetime=models.DateTimeField(auto_now=True)
    task=models.ForeignKey(Task,on_delete=models.CASCADE,null=True,related_name="comment")


class AssignedTask(models.Model):
  
    assigned_to=models.ForeignKey(User,on_delete=models.CASCADE,default="",related_name="assigned_to")
    task_assigned=models.ForeignKey(Task,on_delete=models.CASCADE,related_name="task_assigned",null=True,blank=True)
    assigned_date=models.DateTimeField(auto_now=True)
    # comment=models.ForeignKey(Comment,on_delete=models.CASCADE,null=True,blank=True)

    # def __str__(self) -> str:
    #     return self.task_assigned.task + " " + "To" + " " + self.assigned_to.username


