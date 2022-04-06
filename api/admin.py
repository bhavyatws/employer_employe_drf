
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy  as _
from .models import *
# Register your models here.
from django.contrib.auth import get_user_model
class CustomUserAdmin(UserAdmin):
    '''Define admin model for custom User with no username field'''
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined","employer")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    list_display = ("username",  "first_name", "last_name", "is_staff","employer")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    
admin.site.register(get_user_model(),CustomUserAdmin)


from api.models import Task,Comment,AssignedTask



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['id','task','task_date','task_deadline','user']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['id','comment','task','datetime','user']

@admin.register(AssignedTask)
class AssignedTaskAdmin(admin.ModelAdmin):
    list_display=['id','assigned_to','task_assigned']