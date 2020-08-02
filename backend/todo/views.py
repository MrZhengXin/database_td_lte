# todo/views.py

import pandas as pd

from django.shortcuts import render
from rest_framework import viewsets          # add this
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework import generics 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from drf_renderer_xlsx.renderers import XLSXRenderer
from drf_renderer_xlsx.mixins import XLSXFileMixin

from django.views.generic import ListView
from django.http import HttpResponseRedirect
from bulk_sync import bulk_sync

from .models import Post
from .serializers import *     # add this
from .models import *                     # add this
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

class DownloadTbpciassignmentView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [XLSXRenderer, XLSXFileMixin]

    @staticmethod
    def get(request):
        queryset = Tbpciassignment.objects.all()
        serializer = TbpciassignmentSerializer(queryset, many=True)
        filename = 'Tbpciassignment.xlsx'
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class DownloadTbatuc2IView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [XLSXRenderer, XLSXFileMixin]

    @staticmethod
    def get(request):
        queryset = Tbatuc2I.objects.all()
        serializer = Tbatuc2ISerializer(queryset, many=True)
        filename = 'Tbatuc2I.xlsx'
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class DownloadTbatuhandoverView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [XLSXRenderer, XLSXFileMixin]

    @staticmethod
    def get(request):
        queryset = Tbatuhandover.objects.all()
        serializer = TbatuhandoverSerializer(queryset, many=True)
        filename = 'Tbatuhandover.xlsx'
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class DownloadTboptcellView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [XLSXRenderer, XLSXFileMixin]

    @staticmethod
    def get(request):
        queryset = Tboptcell.objects.all()
        serializer = TboptcellSerializer(queryset, many=True)
        filename = 'Tboptcell.xlsx'
        return Response(data=serializer.data, status=status.HTTP_200_OK)

primary_keys = {'tbCell': 'SECTOR_ID', 
    'tbKPI': ['起始时间',	'周期',	'网元名称',	'小区',	'小区1'],
    'tbPRB': ['起始时间',	'周期',	'网元名称',	'小区',	'小区名'],
    'tbMROData': ['TimeStamp', 'ServingSector', 'InterferingSector']
}

def handle_upload_file(upload_file):
    _, file_name, file_type = upload_file.name.split('.')
    # print(file_name, file_type)
    df = pd.read_excel(upload_file)    
    primary_key = df[primary_keys[file_name]].to_dict('records')
    records = df.to_dict('records')
    if file_name == 'tbCell':
        # print(Tbcell.objects.filter(pk__in=primary_key))
        primary_key = df[primary_keys[file_name]].values.tolist()
        Tbcell.objects.filter(pk__in=primary_key).delete()
        Tbcell.objects.bulk_create(
            [Tbcell(**vals) for vals in records]
        )
    if file_name == 'tbKPI':
        print(primary_key)
        print(Tbkpi.objects.filter(pk__in=primary_key))
        Tbkpi.objects.filter(pk__in=primary_key).delete()
        Tbkpi.objects.bulk_create(
            [Tbkpi(**vals) for vals in df.to_dict('records')]
        )
    if file_name == 'tbPRB':
        for vals in df.to_dict('records'):
            Tbprb.objects.update_or_create(**vals)
    if file_name == 'tbMROData':
        for pk, r in zip(primary_key, records):
            old_obj, created = Tbmrodata.objects.get_or_create(defaults=r, **pk)
            # print(old_obj, created)
            if not created:
                new_obj = Tbmrodata(**r)
                if old_obj != new_obj:
                    old_obj.delete()
                    new_obj.save()



class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)   
    def post(self, request, *args, **kwargs): 
        if len(request.data.keys()) != 0:
            handle_upload_file(request.data['file'])
            return Response(request.data['file'].name, status=status.HTTP_201_CREATED)
        else:
            return Response('empty file', status=status.HTTP_400_BAD_REQUEST)
