# Generated by Django 2.2 on 2020-05-22 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp6', '0013_auto_20200522_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_question',
            name='current_version_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='create_question_history',
            name='version_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
