from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('tasklist/', views.taskList, name='tasklist'),
    path('taskcreate/', views.taskCreate, name='taskcreate'),
    path('taskview/<str:pk>', views.taskView, name='taskview'),
    path('taskupdate/<str:pk>', views.taskUpdate, name='taskupdate'),
    path('taskdelete/<str:pk>', views.taskDelete, name='taskdelete'),
    
]