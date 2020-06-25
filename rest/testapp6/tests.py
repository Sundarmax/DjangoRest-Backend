import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from testapp6.models import create_question



class addQuestionTestCase(APITestCase):

    def test_addNewQuestion(self):
        data = {"ques_type":"blanktype"}
        response = self.client.post("/api/add/question/",data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
