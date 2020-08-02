# todo/serializers.py

from rest_framework import serializers
from .models import *
from backend import settings

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')

class DocumentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Document
        fields = ('docfile', )

class Tbatuc2ISerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbatuc2I
        fields = '__all__'

class TbatudataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbatudata
        fields = '__all__'

class TbatuhandoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbatuhandover
        fields = '__all__'

class TbadjcellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbadjcell
        fields = '__all__'

class Tbc2ISerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbc2I
        fields = '__all__'

class TbcellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbcell
        fields = '__all__'

class TbhandoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbhandover
        fields = '__all__'

class TbmrodataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbmrodata
        fields = '__all__'

class TboptcellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tboptcell
        fields = '__all__'

class TbpciassignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbpciassignment
        fields = '__all__'

class TbpciassignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbpciassignment
        fields = '__all__'

class TbsecadjcellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbsecadjcell
        fields = '__all__'

class TbprbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbprb
        fields = '__all__'

class TbkpiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbkpi
        fields = '__all__'

