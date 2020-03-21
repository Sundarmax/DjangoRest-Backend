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
def user_passes_test(old_fuction):
    def new_function(request, *args, **kwargs):
        try:
            #user_ = User.objects.get(id=1123)
            pass
        except Exception as e:
            return Response('ERROR: user was not exist',status=401)
        return old_fuction(request, *args, **kwargs)
    return new_function

class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

class UserProfileView(RetrieveAPIView):
    
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        #print(request.user.id)
        try:
            user_profile = User.objects.get(id=request.user.id)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                'data': [{
                    'user_name': user_profile.username
                    }]
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
                }
        return Response(response, status=status_code)


# Function based views in django 

@api_view(['GET'])
@permission_classes((AllowAny,))
@user_passes_test
def StudentProfile(request):
    if request.method == 'GET':
        return Response(1)

# Adding a extra fields In MTM relationship table. 
person_ = Person.objects.get(id =1)
print(person_)
group_ = Group.objects.get(id = 1)
print(group_)
person_in_group = group_.members.all()
print(person_in_group)
#m2 = Membership.objects.create(person=person_, group=group_,invite_reason="Wanted to form a band.")
group_.members.clear()
