# Generated by Django 2.1.4 on 2020-04-16 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp5', '0002_auto_20200416_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=155)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('skill_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_topics', to='testapp5.skill_topic')),
            ],
            options={
                'db_table': 'skill',
            },
        ),
    ]
