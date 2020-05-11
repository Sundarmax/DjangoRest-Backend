from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import create_question
from .serializers import *

#from django_filters import rest_framework as filters
#from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class QuestionsAPIView(generics.ListCreateAPIView):
    #search_fields    = ['importance']
    #filter_backends  = (filters.SearchFilter,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['importance','complexity']
    queryset         =  create_question.objects.all()
    serializer_class = QuestionSerializer

