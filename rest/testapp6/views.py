# Create your views here.
from rest_framework import generics

from rest_framework.response import Response
from .models import create_question
from .serializers import *

#from django_filters import rest_framework as filters
#from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    
    page_size = 2
    quizbank_id = None
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })


class QuestionsAPIView(generics.ListCreateAPIView):
    #search_fields    = ['importance']
    #filter_backends  = (filters.SearchFilter,)
    pagination_class  = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['importance','complexity']
    queryset         =  create_question.objects.all()
    serializer_class = QuestionSerializer
    

    def get_queryset(self):
        queryset        = create_question.objects.all().order_by("id")
        return queryset


