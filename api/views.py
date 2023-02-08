from django.shortcuts import render
from .models import *
from rest_framework.generics import ListAPIView
from .serializer import  NewsSerializer
# Create your views here.


class ApiView(ListAPIView):
    queryset=News.objects.all()
    serializer_class= NewsSerializer