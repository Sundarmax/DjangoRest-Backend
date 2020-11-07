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
from django.contrib.auth import authenticate, user_logged_in
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import User
from testapp.models import Person,Group,Membership
import datetime


from django.template import loader
from django.http import HttpResponse
import logging

# from .models import UserLoginActivity
# for logging - define "error" named logging handler and logger in settings.py
from django.contrib.auth import user_logged_in, user_login_failed
from django.dispatch import receiver

error_log = logging.getLogger('error')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@receiver(user_logged_in)
def log_user_logged_in_success(sender, user, request=None, **kwargs):
    print('Singal Received')
    try:
        pass
        user_agent_info = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],
        print(user_agent_info)
        print(get_client_ip(request))
        # user_login_activity_log = UserLoginActivity(login_IP=get_client_ip(request),
        #                                             login_username=user.username,
        #                                             user_agent_info=user_agent_info,
        #                                             status=UserLoginActivity.SUCCESS)
        # user_login_activity_log.save()
    except Exception as e:
        # log the error
        error_log.error("log_user_logged_in request: %s, error: %s" % (request, e))

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

@api_view(['POST'])
@permission_classes((AllowAny,))
def CheckLoginSignal(request):
    if request.method == 'POST':
        user = request.data.get('username')
        password = request.data.get('password')
        if user and password:
            isValid = authenticate(username=user,password=password)
            if isValid:
                user_logged_in.send(sender=isValid.__class__,request=request,user=isValid)
                return Response({"message":"Login Success"})
            else:
                return Response({"message":"Login Fail"})
        else:
            return Response({"message":"keys were not found"})
        return Response(1)

