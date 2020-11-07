from django.shortcuts import render
from django.dispatch import receiver
from .models import UserLoginActivity
from django.contrib.auth import authenticate, user_logged_in

def checkAuthenticate():
    user = authenticate(username='admin',password='admin')
    if user:
        #user_logged_in.send(sender=user.__class__, user=user)
        user_logged_in.send(sender=user.__class__, user=user)
        print("Send login success signal")
    else:
        print('Fail')

#checkAuthenticate()