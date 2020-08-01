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
    path('admin/', admin.site.urls),         
    # path('api/', include(router.urls)),
    # path('', include('todo.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('rest_registration.api.urls')),
    url(r'^upload/$', views.FileUploadView.as_view(), name='file-upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)