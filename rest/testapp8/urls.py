from django.conf.urls import url
from django.urls import path
from testapp8.views import *

urlpatterns = [
    path('test/',CustomerProfile),   
]
