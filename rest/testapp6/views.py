# Create your views here.
from rest_framework import generics

from rest_framework.response import Response
from .models import create_question
from .serializers import *

#from django_filters import rest_framework as filters
#from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.pagination import PageNumberPagination

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,views
from rest_framework.decorators import action,api_view, permission_classes
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    DjangoModelPermissions,
    DjangoModelPermissionsOrAnonReadOnly
    )

class CustomPagination(PageNumberPagination):
    
    page_size = 10
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
    filterset_fields = {
            'importance' : ['exact', 'lte', 'gte'],
            'created_at' : ['exact', 'lte', 'gte']
    }
    queryset         =  create_question.objects.all()
    serializer_class = QuestionSerializer
    

    def get_queryset(self):
        queryset        = create_question.objects.all().order_by("id")
        return queryset
    
@api_view(['POST'])
@permission_classes((AllowAny,))
def add_new_question(request):
    if request.method == "POST":
        _payload = QuestionSerializer(data=request.data)
        if _payload.is_valid():

            return Response({"isError": False}, status=status.HTTP_200_OK)
        else:
            return Response({"isError": True, "errors": _payload.errors}, status=status.HTTP_400_BAD_REQUEST)