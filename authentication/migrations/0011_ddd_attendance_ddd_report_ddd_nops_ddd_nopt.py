# Generated by Django 4.0.6 on 2022-07-29 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_ddd_personone_ddd_persontree_ddd_persontwo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ddd',
            name='Attendance',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ddd',
            name='Report',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ddd',
            name='nops',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ddd',
            name='nopt',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
