# Generated by Django 4.1 on 2023-03-21 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0007_alter_user_registration_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_registration',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
