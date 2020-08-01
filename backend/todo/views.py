# todo/views.py

from django.shortcuts import render
from rest_framework import viewsets          # add this
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework import generics 
from rest_framework import status
from rest_framework.response import Response

from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .models import Post
from .serializers import TodoSerializer, DocumentSerializer      # add this
from .models import Todo                     # add this
from .forms import PostForm # new

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new

class TodoView(viewsets.ModelViewSet):       # add this
    serializer_class = TodoSerializer          # add this
    queryset = Todo.objects.all()              # add this

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)   
    def post(self, request, *args, **kwargs):       
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            return Response('upload successfully', status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
