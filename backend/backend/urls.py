"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  
from rest_framework import routers
from django.conf.urls import url
from todo import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# router = routers.DefaultRouter()    
# router.register(r'todos', views.TodoView, 'todo') 

urlpatterns = [
    path('admin/', admin.site.urls, name='administration'),         
    # path('api/', include(router.urls)),
    # path('', include('todo.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('rest_registration.api.urls')),
    url(r'^upload/$', views.FileUploadView.as_view(), name='file-upload'),
    url(r'^download/tbATUC2I', views.DownloadTbatuc2IView.as_view(), name='tbATUC2I download'),
    url(r'^download/tbPCIAssignment', views.DownloadTbpciassignmentView.as_view(), name='tbPCIAssignment download'),
    url(r'^download/tbATUHandOver', views.DownloadTbatuhandoverView.as_view(), name='tbATUHandOver download'),
    url(r'^download/tbOptCell', views.DownloadTboptcellView.as_view(), name='tbOptCell download'),
    url(r'query/tbCell/', views.QueryTbCellView.as_view(), name='query tbCell'),
    url(r'query/tbKPI/', views.QueryTbkpiView.as_view(), name='query tbKPI'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)