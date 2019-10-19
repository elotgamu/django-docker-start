# Generated by Django 2.2.6 on 2019-10-18 17:08
import os
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    def generate_superuser(apps, schema_editor):
        """ Set up a superuser in migration """
        from django.contrib.auth import get_user_model

        DJANGO_DB_NAME = os.environ.get("DJANGO_DB_NAME", "default")
        DJANGO_ROOT_USERNAME = os.environ.get("DJANGO_ROOT_USERNAME")
        DJANGO_ROOT_EMAIL = os.environ.get("DJANGO_ROOT_EMAIL")
        DJANGO_ROOT_PASSWORD = os.environ.get("DJANGO_ROOT_PASSWORD")
        User = get_user_model()

        superuser = User.objects.create_superuser(
            username=DJANGO_ROOT_USERNAME,
            email=DJANGO_ROOT_EMAIL,
            password=DJANGO_ROOT_PASSWORD
        )
        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]
