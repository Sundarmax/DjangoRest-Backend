from django.conf.urls import url
from testapp.views import *

urlpatterns = [
    url(r'^signin', UserLoginView.as_view()),
    url(r'^profile', UserProfileView.as_view())
]