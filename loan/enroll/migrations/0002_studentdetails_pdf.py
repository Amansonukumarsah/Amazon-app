# Generated by Django 3.2 on 2021-11-26 15:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='pdf',
            field=models.FileField(default=django.utils.timezone.now, upload_to='pdfs/'),
            preserve_default=False,
        ),
    ]
