from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from testapp.serializers import UserLoginSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import User
from testapp.models import Person,Group,Membership
import datetime


from django.template import loader
from django.http import HttpResponse

# use custom response class to override HttpResponse.close()
class LogSuccessResponse(HttpResponse):
    testData =  None

    def close(self):
        super(LogSuccessResponse, self).close()
        # do whatever you want, this is the last codepoint in request handling
        if self.status_code == 200:
            print('HttpResponse successful: %s' % self.status_code)

# this would be the view definition
def logging_view(request):
    pass


'''
Execute code after response sent to client
'''

@api_view(['GET','POST'])
@permission_classes((AllowAny,))
def CustomerProfile(request):
    if request.method == 'GET':
        #testIns = LogSuccessResponse(instance=1)
        response = LogSuccessResponse('Hello World') 
        return response
    if request.method == 'POST':
        return Response(2)
