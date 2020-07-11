# Create your views here.
from rest_framework import generics

from rest_framework.response import Response
from .models import create_question,create_question_history
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

from datetime import datetime
from django.utils import timezone

#import datetime
import pytz

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
            'created_at' : ['exact', 'lte', 'gte'],
            'updated_at' : ['exact','date','lte','gte'],
    }
    queryset         =  create_question.objects.all()
    serializer_class = QuestionSerializer
    

    def get_queryset(self):
        queryset        = create_question.objects.filter().order_by("id")
        return queryset
    
@api_view(['POST','PATCH'] )
@permission_classes((AllowAny,))
def add_new_question(request):
    if request.method == "POST":
        _payload = QuestionSerializer(data=request.data)
        if _payload.is_valid():
            _payload.save()
            return Response({"isError": False}, status=status.HTTP_201_CREATED)
        else:
            return Response({"isError": True, "errors": _payload.errors}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PATCH":
        data = create_question.objects.get(id = 19)
        print(data.updated_at)
        serializer = QuestionSerializer(data, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def CheckTimeZone():
    time_zone = pytz.timezone('Asia/Kolkata')
    data = create_question_history.objects.get(id=5)
    print("Record UTC Time" ,data.submitted )
    print("<--------------------------------->")
    #print("current time is ", datetime.now())
    print("UTC time is ", timezone.now())
    diff = timezone.now().timestamp() - data.submitted.timestamp()
    print(diff)
    print("<--------------------------------->")

def ConvertTimeZone():
    time_zone = pytz.timezone('Asia/Kolkata')
    # get naive date
    #date = datetime.datetime.now().date()
    # get naive time
    #time = datetime.time(date.hour,date.minute)
    # combite to datetime
    #date_time = datetime.datetime.combine(date, time)
    # make time zone aware
    date_time = time_zone.localize(datetime.now())
    # convert to UTC
    utc_date_time = date_time.astimezone(pytz.utc)
    # get time
    utc_time = utc_date_time.time()
    print(date_time)
    print(utc_date_time)
    print(utc_time)

def addQuestion():
    try:
        add = create_question_history()
        add.ques_type = "mcq"
        add.importance = 2
        add.created_at = timezone.now()
        add.save()
        print('Record saved')
    except Exception as e:
        print(e)


def CheckDynamicFilter():
    searchDict = {}
    #qs_type = request.query_params.get('ques_type', None)
    qs_type = None
    if qs_type:
        searchDict["ques_type"] = qs_type
    quesIns = create_question.objects.filter(**searchDict)    
    print(quesIns)
    