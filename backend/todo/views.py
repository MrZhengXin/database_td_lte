# todo/views.py

import pandas as pd
import datetime

from django.shortcuts import render
from django.db import connection
from rest_framework import viewsets          # add this
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser
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

cursor = connection.cursor()


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

class QueryTbCellView(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request):
        attribute, value = request.GET.get('attribute'), request.GET.get('value')
        if value == "-1":
            data = Tbcell.objects.values_list(attribute)
        else:
            data = Tbcell.objects.filter(**{attribute: value}).values()

        return Response(data)

class QueryTbkpiView(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request):
        attribute_list = request.GET.get('attribute_list', False)
        if attribute_list:
            return Response([f.name for f in Tbkpi._meta.get_fields() 
                if f.name not in Tbkpi._meta.unique_together[0]])
        NE_list = request.GET.get('NE_list', False)
        if NE_list:
            return Response(Tbkpi.objects.values_list('小区1'))
        NE, attribute = request.GET.get('NE', None), request.GET.get('attribute', None)
        l, r = request.GET.get('l', None), request.GET.get('r', None)
        l = datetime.datetime.strptime(l, '%m/%d/%Y %H:%M:%S')
        r = datetime.datetime.strptime(r, '%m/%d/%Y %H:%M:%S')
        data = Tbkpi.objects.filter(小区1=NE).filter(起始时间__range=(l, r))
        if attribute is not None:
            data = data.values_list('起始时间', attribute)
        return Response(data)

class CreateDownloadTbc2InewView(APIView):
    renderer_classes = [XLSXRenderer, XLSXFileMixin]

    @staticmethod
    def get(request):
        minimum = request.GET.get('minimum', 5)
        with connection.cursor() as cursor:
            cursor.execute('exec [dbo].[C2I_Analyse] %s' % (minimum))
        queryset = Tbc2Inew.objects.all()
        serializer = Tbc2InewSerializer(queryset, many=True)
        filename = 'Tbc2Inew.xlsx'
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class CreateDownloadTbc2I3View(APIView):
    renderer_classes = [XLSXRenderer, XLSXFileMixin]

    @staticmethod
    def get(request):
        rate = request.GET.get('rate', "0.7")
        with connection.cursor() as cursor:
            cursor.execute('exec [dbo].[generate_triSector] %s' % (rate))
        queryset = Tbc2I3.objects.all()
        serializer = Tbc2I3Serializer(queryset, many=True)
        filename = 'Tbc2I3.xlsx'
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CreateDownloadTbprbnewView(APIView):
    renderer_classes = [XLSXRenderer, XLSXFileMixin]

    @staticmethod
    def get(request):
        queryset = Tbprbnew.objects.all()
        if len(queryset) == 0:
            with connection.cursor() as cursor:
                cursor.execute('''
    INSERT  INTO [tbPRBnew] 
    select [c].[起始时间],[周期],[网元名称],[小区],[b].[小区名],
    [第0个prb上检测到的干扰噪声的平均值_field], [第1个prb上检测到的干扰噪声的平均值_field], [第2个prb上检测到的干扰噪声的平均值_field], [第3个prb上检测到的干扰噪声的平均值_field], [第4个prb上检测到的干扰噪声的平均值_field], [第5个prb上检测到的干扰噪声的平均值_field], [第6个prb上检测到的干扰噪声的平均值_field], [第7个prb上检测到的干扰噪声的平均值_field], [第8个prb上检测到的干扰噪声的平均值_field], [第9个prb上检测到的干扰噪声的平均值_field],
    [第10个prb上检测到的干扰噪声的平均值_field], [第11个prb上检测到的干扰噪声的平均值_field], [第12个prb上检测到的干扰噪声的平均值_field], [第13个prb上检测到的干扰噪声的平均值_field], [第14个prb上检测到的干扰噪声的平均值_field], [第15个prb上检测到的干扰噪声的平均值_field], [第16个prb上检测到的干扰噪声的平均值_field], [第17个prb上检测到的干扰噪声的平均值_field], [第18个prb上检测到的干扰噪声的平均值_field], [第19个prb上检测到的干扰噪声的平均值_field],
    [第20个prb上检测到的干扰噪声的平均值_field], [第21个prb上检测到的干扰噪声的平均值_field], [第22个prb上检测到的干扰噪声的平均值_field], [第23个prb上检测到的干扰噪声的平均值_field], [第24个prb上检测到的干扰噪声的平均值_field], [第25个prb上检测到的干扰噪声的平均值_field], [第26个prb上检测到的干扰噪声的平均值_field], [第27个prb上检测到的干扰噪声的平均值_field], [第28个prb上检测到的干扰噪声的平均值_field], [第29个prb上检测到的干扰噪声的平均值_field],
    [第30个prb上检测到的干扰噪声的平均值_field], [第31个prb上检测到的干扰噪声的平均值_field], [第32个prb上检测到的干扰噪声的平均值_field], [第33个prb上检测到的干扰噪声的平均值_field], [第34个prb上检测到的干扰噪声的平均值_field], [第35个prb上检测到的干扰噪声的平均值_field], [第36个prb上检测到的干扰噪声的平均值_field], [第37个prb上检测到的干扰噪声的平均值_field], [第38个prb上检测到的干扰噪声的平均值_field], [第39个prb上检测到的干扰噪声的平均值_field],
    [第40个prb上检测到的干扰噪声的平均值_field], [第41个prb上检测到的干扰噪声的平均值_field], [第42个prb上检测到的干扰噪声的平均值_field], [第43个prb上检测到的干扰噪声的平均值_field], [第44个prb上检测到的干扰噪声的平均值_field], [第45个prb上检测到的干扰噪声的平均值_field], [第46个prb上检测到的干扰噪声的平均值_field], [第47个prb上检测到的干扰噪声的平均值_field], [第48个prb上检测到的干扰噪声的平均值_field], [第49个prb上检测到的干扰噪声的平均值_field],
    [第50个prb上检测到的干扰噪声的平均值_field], [第51个prb上检测到的干扰噪声的平均值_field], [第52个prb上检测到的干扰噪声的平均值_field], [第53个prb上检测到的干扰噪声的平均值_field], [第54个prb上检测到的干扰噪声的平均值_field], [第55个prb上检测到的干扰噪声的平均值_field], [第56个prb上检测到的干扰噪声的平均值_field], [第57个prb上检测到的干扰噪声的平均值_field], [第58个prb上检测到的干扰噪声的平均值_field], [第59个prb上检测到的干扰噪声的平均值_field],
    [第60个prb上检测到的干扰噪声的平均值_field], [第61个prb上检测到的干扰噪声的平均值_field], [第62个prb上检测到的干扰噪声的平均值_field], [第63个prb上检测到的干扰噪声的平均值_field], [第64个prb上检测到的干扰噪声的平均值_field], [第65个prb上检测到的干扰噪声的平均值_field], [第66个prb上检测到的干扰噪声的平均值_field], [第67个prb上检测到的干扰噪声的平均值_field], [第68个prb上检测到的干扰噪声的平均值_field], [第69个prb上检测到的干扰噪声的平均值_field],
    [第70个prb上检测到的干扰噪声的平均值_field], [第71个prb上检测到的干扰噪声的平均值_field], [第72个prb上检测到的干扰噪声的平均值_field], [第73个prb上检测到的干扰噪声的平均值_field], [第74个prb上检测到的干扰噪声的平均值_field], [第75个prb上检测到的干扰噪声的平均值_field], [第76个prb上检测到的干扰噪声的平均值_field], [第77个prb上检测到的干扰噪声的平均值_field], [第78个prb上检测到的干扰噪声的平均值_field], [第79个prb上检测到的干扰噪声的平均值_field],
    [第80个prb上检测到的干扰噪声的平均值_field], [第81个prb上检测到的干扰噪声的平均值_field], [第82个prb上检测到的干扰噪声的平均值_field], [第83个prb上检测到的干扰噪声的平均值_field], [第84个prb上检测到的干扰噪声的平均值_field], [第85个prb上检测到的干扰噪声的平均值_field], [第86个prb上检测到的干扰噪声的平均值_field], [第87个prb上检测到的干扰噪声的平均值_field], [第88个prb上检测到的干扰噪声的平均值_field], [第89个prb上检测到的干扰噪声的平均值_field],
    [第90个prb上检测到的干扰噪声的平均值_field], [第91个prb上检测到的干扰噪声的平均值_field], [第92个prb上检测到的干扰噪声的平均值_field], [第93个prb上检测到的干扰噪声的平均值_field], [第94个prb上检测到的干扰噪声的平均值_field], [第95个prb上检测到的干扰噪声的平均值_field], [第96个prb上检测到的干扰噪声的平均值_field], [第97个prb上检测到的干扰噪声的平均值_field], [第98个prb上检测到的干扰噪声的平均值_field], [第99个prb上检测到的干扰噪声的平均值_field]
from(
        select [小区名],	DATEPART(HOUR,[起始时间]) as hour,DATEPART(DAY,[起始时间])as day,DATEPART(MONTH,[起始时间])as month,DATEPART(YEAR,[起始时间]) as year,
            avg([第0个prb上检测到的干扰噪声的平均值_field]) as [第0个prb上检测到的干扰噪声的平均值_field], avg([第1个prb上检测到的干扰噪声的平均值_field]) as [第1个prb上检测到的干扰噪声的平均值_field], avg([第2个prb上检测到的干扰噪声的平均值_field]) as [第2个prb上检测到的干扰噪声的平均值_field], avg([第3个prb上检测到的干扰噪声的平均值_field]) as [第3个prb上检测到的干扰噪声的平均值_field], avg([第4个prb上检测到的干扰噪声的平均值_field]) as [第4个prb上检测到的干扰噪声的平均值_field], avg([第5个prb上检测到的干扰噪声的平均值_field]) as [第5个prb上检测到的干扰噪声的平均值_field], avg([第6个prb上检测到的干扰噪声的平均值_field]) as [第6个prb上检测到的干扰噪声的平均值_field], avg([第7个prb上检测到的干扰噪声的平均值_field]) as [第7个prb上检测到的干扰噪声的平均值_field], avg([第8个prb上检测到的干扰噪声的平均值_field]) as [第8个prb上检测到的干扰噪声的平均值_field], avg([第9个prb上检测到的干扰噪声的平均值_field]) as [第9个prb上检测到的干扰噪声的平均值_field], 
            avg([第10个prb上检测到的干扰噪声的平均值_field]) as [第10个prb上检测到的干扰噪声的平均值_field], avg([第11个prb上检测到的干扰噪声的平均值_field]) as [第11个prb上检测到的干扰噪声的平均值_field], avg([第12个prb上检测到的干扰噪声的平均值_field]) as [第12个prb上检测到的干扰噪声的平均值_field], avg([第13个prb上检测到的干扰噪声的平均值_field]) as [第13个prb上检测到的干扰噪声的平均值_field], avg([第14个prb上检测到的干扰噪声的平均值_field]) as [第14个prb上检测到的干扰噪声的平均值_field], avg([第15个prb上检测到的干扰噪声的平均值_field]) as [第15个prb上检测到的干扰噪声的平均值_field], avg([第16个prb上检测到的干扰噪声的平均值_field]) as [第16个prb上检测到的干扰噪声的平均值_field], avg([第17个prb上检测到的干扰噪声的平均值_field]) as [第17个prb上检测到的干扰噪声的平均值_field], avg([第18个prb上检测到的干扰噪声的平均值_field]) as [第18个prb上检测到的干扰噪声的平均值_field], avg([第19个prb上检测到的干扰噪声的平均值_field]) as [第19个prb上检测到的干扰噪声的平均值_field], 
            avg([第20个prb上检测到的干扰噪声的平均值_field]) as [第20个prb上检测到的干扰噪声的平均值_field], avg([第21个prb上检测到的干扰噪声的平均值_field]) as [第21个prb上检测到的干扰噪声的平均值_field], avg([第22个prb上检测到的干扰噪声的平均值_field]) as [第22个prb上检测到的干扰噪声的平均值_field], avg([第23个prb上检测到的干扰噪声的平均值_field]) as [第23个prb上检测到的干扰噪声的平均值_field], avg([第24个prb上检测到的干扰噪声的平均值_field]) as [第24个prb上检测到的干扰噪声的平均值_field], avg([第25个prb上检测到的干扰噪声的平均值_field]) as [第25个prb上检测到的干扰噪声的平均值_field], avg([第26个prb上检测到的干扰噪声的平均值_field]) as [第26个prb上检测到的干扰噪声的平均值_field], avg([第27个prb上检测到的干扰噪声的平均值_field]) as [第27个prb上检测到的干扰噪声的平均值_field], avg([第28个prb上检测到的干扰噪声的平均值_field]) as [第28个prb上检测到的干扰噪声的平均值_field], avg([第29个prb上检测到的干扰噪声的平均值_field]) as [第29个prb上检测到的干扰噪声的平均值_field], 
            avg([第30个prb上检测到的干扰噪声的平均值_field]) as [第30个prb上检测到的干扰噪声的平均值_field], avg([第31个prb上检测到的干扰噪声的平均值_field]) as [第31个prb上检测到的干扰噪声的平均值_field], avg([第32个prb上检测到的干扰噪声的平均值_field]) as [第32个prb上检测到的干扰噪声的平均值_field], avg([第33个prb上检测到的干扰噪声的平均值_field]) as [第33个prb上检测到的干扰噪声的平均值_field], avg([第34个prb上检测到的干扰噪声的平均值_field]) as [第34个prb上检测到的干扰噪声的平均值_field], avg([第35个prb上检测到的干扰噪声的平均值_field]) as [第35个prb上检测到的干扰噪声的平均值_field], avg([第36个prb上检测到的干扰噪声的平均值_field]) as [第36个prb上检测到的干扰噪声的平均值_field], avg([第37个prb上检测到的干扰噪声的平均值_field]) as [第37个prb上检测到的干扰噪声的平均值_field], avg([第38个prb上检测到的干扰噪声的平均值_field]) as [第38个prb上检测到的干扰噪声的平均值_field], avg([第39个prb上检测到的干扰噪声的平均值_field]) as [第39个prb上检测到的干扰噪声的平均值_field], 
            avg([第40个prb上检测到的干扰噪声的平均值_field]) as [第40个prb上检测到的干扰噪声的平均值_field], avg([第41个prb上检测到的干扰噪声的平均值_field]) as [第41个prb上检测到的干扰噪声的平均值_field], avg([第42个prb上检测到的干扰噪声的平均值_field]) as [第42个prb上检测到的干扰噪声的平均值_field], avg([第43个prb上检测到的干扰噪声的平均值_field]) as [第43个prb上检测到的干扰噪声的平均值_field], avg([第44个prb上检测到的干扰噪声的平均值_field]) as [第44个prb上检测到的干扰噪声的平均值_field], avg([第45个prb上检测到的干扰噪声的平均值_field]) as [第45个prb上检测到的干扰噪声的平均值_field], avg([第46个prb上检测到的干扰噪声的平均值_field]) as [第46个prb上检测到的干扰噪声的平均值_field], avg([第47个prb上检测到的干扰噪声的平均值_field]) as [第47个prb上检测到的干扰噪声的平均值_field], avg([第48个prb上检测到的干扰噪声的平均值_field]) as [第48个prb上检测到的干扰噪声的平均值_field], avg([第49个prb上检测到的干扰噪声的平均值_field]) as [第49个prb上检测到的干扰噪声的平均值_field], 
            avg([第50个prb上检测到的干扰噪声的平均值_field]) as [第50个prb上检测到的干扰噪声的平均值_field], avg([第51个prb上检测到的干扰噪声的平均值_field]) as [第51个prb上检测到的干扰噪声的平均值_field], avg([第52个prb上检测到的干扰噪声的平均值_field]) as [第52个prb上检测到的干扰噪声的平均值_field], avg([第53个prb上检测到的干扰噪声的平均值_field]) as [第53个prb上检测到的干扰噪声的平均值_field], avg([第54个prb上检测到的干扰噪声的平均值_field]) as [第54个prb上检测到的干扰噪声的平均值_field], avg([第55个prb上检测到的干扰噪声的平均值_field]) as [第55个prb上检测到的干扰噪声的平均值_field], avg([第56个prb上检测到的干扰噪声的平均值_field]) as [第56个prb上检测到的干扰噪声的平均值_field], avg([第57个prb上检测到的干扰噪声的平均值_field]) as [第57个prb上检测到的干扰噪声的平均值_field], avg([第58个prb上检测到的干扰噪声的平均值_field]) as [第58个prb上检测到的干扰噪声的平均值_field], avg([第59个prb上检测到的干扰噪声的平均值_field]) as [第59个prb上检测到的干扰噪声的平均值_field], 
            avg([第60个prb上检测到的干扰噪声的平均值_field]) as [第60个prb上检测到的干扰噪声的平均值_field], avg([第61个prb上检测到的干扰噪声的平均值_field]) as [第61个prb上检测到的干扰噪声的平均值_field], avg([第62个prb上检测到的干扰噪声的平均值_field]) as [第62个prb上检测到的干扰噪声的平均值_field], avg([第63个prb上检测到的干扰噪声的平均值_field]) as [第63个prb上检测到的干扰噪声的平均值_field], avg([第64个prb上检测到的干扰噪声的平均值_field]) as [第64个prb上检测到的干扰噪声的平均值_field], avg([第65个prb上检测到的干扰噪声的平均值_field]) as [第65个prb上检测到的干扰噪声的平均值_field], avg([第66个prb上检测到的干扰噪声的平均值_field]) as [第66个prb上检测到的干扰噪声的平均值_field], avg([第67个prb上检测到的干扰噪声的平均值_field]) as [第67个prb上检测到的干扰噪声的平均值_field], avg([第68个prb上检测到的干扰噪声的平均值_field]) as [第68个prb上检测到的干扰噪声的平均值_field], avg([第69个prb上检测到的干扰噪声的平均值_field]) as [第69个prb上检测到的干扰噪声的平均值_field], 
            avg([第70个prb上检测到的干扰噪声的平均值_field]) as [第70个prb上检测到的干扰噪声的平均值_field], avg([第71个prb上检测到的干扰噪声的平均值_field]) as [第71个prb上检测到的干扰噪声的平均值_field], avg([第72个prb上检测到的干扰噪声的平均值_field]) as [第72个prb上检测到的干扰噪声的平均值_field], avg([第73个prb上检测到的干扰噪声的平均值_field]) as [第73个prb上检测到的干扰噪声的平均值_field], avg([第74个prb上检测到的干扰噪声的平均值_field]) as [第74个prb上检测到的干扰噪声的平均值_field], avg([第75个prb上检测到的干扰噪声的平均值_field]) as [第75个prb上检测到的干扰噪声的平均值_field], avg([第76个prb上检测到的干扰噪声的平均值_field]) as [第76个prb上检测到的干扰噪声的平均值_field], avg([第77个prb上检测到的干扰噪声的平均值_field]) as [第77个prb上检测到的干扰噪声的平均值_field], avg([第78个prb上检测到的干扰噪声的平均值_field]) as [第78个prb上检测到的干扰噪声的平均值_field], avg([第79个prb上检测到的干扰噪声的平均值_field]) as [第79个prb上检测到的干扰噪声的平均值_field], 
            avg([第80个prb上检测到的干扰噪声的平均值_field]) as [第80个prb上检测到的干扰噪声的平均值_field], avg([第81个prb上检测到的干扰噪声的平均值_field]) as [第81个prb上检测到的干扰噪声的平均值_field], avg([第82个prb上检测到的干扰噪声的平均值_field]) as [第82个prb上检测到的干扰噪声的平均值_field], avg([第83个prb上检测到的干扰噪声的平均值_field]) as [第83个prb上检测到的干扰噪声的平均值_field], avg([第84个prb上检测到的干扰噪声的平均值_field]) as [第84个prb上检测到的干扰噪声的平均值_field], avg([第85个prb上检测到的干扰噪声的平均值_field]) as [第85个prb上检测到的干扰噪声的平均值_field], avg([第86个prb上检测到的干扰噪声的平均值_field]) as [第86个prb上检测到的干扰噪声的平均值_field], avg([第87个prb上检测到的干扰噪声的平均值_field]) as [第87个prb上检测到的干扰噪声的平均值_field], avg([第88个prb上检测到的干扰噪声的平均值_field]) as [第88个prb上检测到的干扰噪声的平均值_field], avg([第89个prb上检测到的干扰噪声的平均值_field]) as [第89个prb上检测到的干扰噪声的平均值_field], 
            avg([第90个prb上检测到的干扰噪声的平均值_field]) as [第90个prb上检测到的干扰噪声的平均值_field], avg([第91个prb上检测到的干扰噪声的平均值_field]) as [第91个prb上检测到的干扰噪声的平均值_field], avg([第92个prb上检测到的干扰噪声的平均值_field]) as [第92个prb上检测到的干扰噪声的平均值_field], avg([第93个prb上检测到的干扰噪声的平均值_field]) as [第93个prb上检测到的干扰噪声的平均值_field], avg([第94个prb上检测到的干扰噪声的平均值_field]) as [第94个prb上检测到的干扰噪声的平均值_field], avg([第95个prb上检测到的干扰噪声的平均值_field]) as [第95个prb上检测到的干扰噪声的平均值_field], avg([第96个prb上检测到的干扰噪声的平均值_field]) as [第96个prb上检测到的干扰噪声的平均值_field], avg([第97个prb上检测到的干扰噪声的平均值_field]) as [第97个prb上检测到的干扰噪声的平均值_field], avg([第98个prb上检测到的干扰噪声的平均值_field]) as [第98个prb上检测到的干扰噪声的平均值_field], avg([第99个prb上检测到的干扰噪声的平均值_field]) as [第99个prb上检测到的干扰噪声的平均值_field]
        from [tbPRB]
        group by DATEPART(HOUR,[起始时间]),DATEPART(DAY,[起始时间]),DATEPART(MONTH,[起始时间]),DATEPART(YEAR,[起始时间]),[小区名]
     )
		 as [b],
		 (select [起始时间],[周期],[网元名称],[小区],[小区名] from [tbPRB]) as [c]
    where  DATEPART(MINUTE, [c].[起始时间])=0 and hour=DATEPART(HOUR,[c].[起始时间]) and day=DATEPART(DAY,[c].[起始时间])  and [b].[小区名]=[c].[小区名]''')
        serializer = TbprbnewSerializer(queryset, many=True)
        filename = 'Tbprbnew.xlsx'
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class QueryTbprbView(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request):
        attribute_list = request.GET.get('attribute_list', False)
        if attribute_list:
            return Response([f.name for f in Tbprb._meta.get_fields() 
                if f.name not in Tbprb._meta.unique_together[0]])
        NE, attribute = request.GET.get('NE', None), request.GET.get('attribute', None)
        l, r = request.GET.get('l', None), request.GET.get('r', None)
        l = datetime.datetime.strptime(l, '%m/%d/%Y %H:%M:%S')
        r = datetime.datetime.strptime(r, '%m/%d/%Y %H:%M:%S')
        data = Tbprb.objects.filter(小区名=NE).filter(起始时间__range=(l, r))
        if attribute is not None:
            data = data.values_list('起始时间', attribute)
        return Response(data)

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
    # cursor = connection.cursor()

    if file_type == 'xlsx':
        df = pd.read_excel(upload_file)    
        values = df.values.tolist()
        query = "INSERT INTO %s VALUES" % file_name +  r" (%s" + r", %s" * (len(values[0])-1) + ")"
        cursor.executemany(query, values)
    else:
        for df in pd.read_csv(upload_file, chunksize=50):
            values = df.values.tolist()
            query = "INSERT INTO %s VALUES" % file_name +  r" (%s" + r", %s" * (len(values[0])-1) + ")"
            cursor.executemany(query, values)





class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)   
    def post(self, request, *args, **kwargs): 
        if len(request.data.keys()) != 0:
            handle_upload_file(request.data['file'])
            return Response(request.data['file'].name, status=status.HTTP_201_CREATED)
        else:
            return Response('empty file', status=status.HTTP_400_BAD_REQUEST)
