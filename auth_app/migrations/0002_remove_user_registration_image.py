# Generated by Django 4.1 on 2023-03-20 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_registration',
            name='image',
        ),
    ]
