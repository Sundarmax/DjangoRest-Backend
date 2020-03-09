from django.conf.urls import url
from testapp.views import *
from django.urls import path

urlpatterns = [
    url(r'^signin', UserLoginView.as_view()),
    url(r'^profile', UserProfileView.as_view()),
    path('student-profile', StudentProfile)

]