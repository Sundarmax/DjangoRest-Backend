from rest_framework import serializers
from testapp6.models import create_question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = create_question
        fields = '__all__'


    