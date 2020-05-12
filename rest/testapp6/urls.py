from django.conf.urls import url
from testapp6.models import *
from django.urls import path
from testapp6 import views
from testapp6.views import add_new_question
urlpatterns = [
    path('questions/', views.QuestionsAPIView.as_view()),
    path('add/question/', add_new_question)
]
