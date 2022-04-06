
from django.urls import path,include
from api import views
from rest_framework_simplejwt import views as jwt_views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('taskapi',views.AddTask,basename='task')
router.register('commentapi',views.Comment,basename='comment')
# router.register('assignedtaskto',views.AssignedTaskTo,basename='assignedtaskto')

urlpatterns = [
    path('',include(router.urls)),
    path('get-token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('api-token-refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('userlist/',views.UserList.as_view(),name="userlist"),
    path('assigntask-employee/',views.CreateAssignedTaskTo.as_view(),name="assigntask-employee"),
    path('get-assignedtask/',views.ListAssignedTaskTo.as_view(),name="get-assignedtask"),
    path('get-comment/',views.GetList.as_view(),name="get-comment"),
    path('get-assignedtask-detail/',views.GetAssignedList.as_view(),name="get-assignedtask-detail"),
    
    
    # path('admin/', admin.site.urls),
]
