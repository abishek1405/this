# Generated by Django 4.0.6 on 2022-07-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_remove_ddd_alumnilecturer_remove_ddd_fdp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ddd',
            name='Upload_Photo_file',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ddd',
            name='fil',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]