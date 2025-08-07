from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("list/", views.linkList, name='list'),
    path("view/<str:pk>/", views.view, name='view'),
    path("delete/<str:pk>/", views.delete, name='delete'),
    path("create/", views.create, name='create'),
    path("getUser/", views.getUser, name='get-user'),
    path("updatetitle/<str:pk>/", views.updatetitle, name='updatetitle'),
   

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)