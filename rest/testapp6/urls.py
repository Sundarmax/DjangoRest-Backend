from django.conf.urls import url
from testapp6.models import *
from django.urls import path
from testapp6 import views

urlpatterns = [
    path('questions/', views.QuestionsAPIView.as_view())
]