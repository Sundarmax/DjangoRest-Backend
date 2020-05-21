from django.contrib import admin

from testapp6.models import create_question,create_question_history
# Register your models here.

admin.site.register(create_question)
admin.site.register(create_question_history)
