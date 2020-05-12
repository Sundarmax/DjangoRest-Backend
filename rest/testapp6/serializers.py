from rest_framework import serializers
from testapp6.models import create_question

class QuestionSerializer(serializers.ModelSerializer):
    
    #question_importance = serializers.IntegerField(source='importance')

    #question_importance = serializers.IntegerField(required=False)

    class Meta:
        model = create_question
        fields = '__all__'


    