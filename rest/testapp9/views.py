from django.shortcuts import render

# Create your views here.
import json
from zoomus import ZoomClient


def Test():
    client = ZoomClient(API_KEY, API_SECRET)
    user_list_response = client.user.list()
    user_list = json.loads(user_list_response.content)
    print(user_list)
    #for user in user_list['users']:
    #user_id = user['id']
    #print(json.loads(client.meeting.list(user_id=user_id).content))

Test()
