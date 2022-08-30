# Generated by Django 4.0.6 on 2022-07-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_ddd_attendance_ddd_report_ddd_nops_ddd_nopt'),
    ]

    operations = [
        migrations.CreateModel(
            name='facultyAttended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FacultyName', models.CharField(max_length=40)),
                ('event', models.CharField(max_length=100)),
                ('Title', models.CharField(max_length=100)),
                ('Place', models.CharField(max_length=100)),
                ('fdatee', models.DateField()),
                ('tdate', models.DateField()),
                ('certificate', models.FileField(upload_to='')),
            ],
        ),
    ]
