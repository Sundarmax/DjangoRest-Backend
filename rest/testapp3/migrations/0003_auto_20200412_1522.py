# Generated by Django 2.1.4 on 2020-04-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp3', '0002_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=100)),
                ('established_on', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('pay', models.PositiveIntegerField()),
                ('joined_on', models.DateField()),
                ('department', models.ForeignKey(on_delete='DO_NOTHING', to='testapp3.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_day', models.DateField()),
                ('employee', models.ForeignKey(on_delete='DO_NOTHING', to='testapp3.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(max_length=100)),
                ('pay_min', models.PositiveIntegerField()),
                ('pay_max', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='level',
            field=models.ForeignKey(on_delete='DO_NOTHING', to='testapp3.Level'),
        ),
    ]
