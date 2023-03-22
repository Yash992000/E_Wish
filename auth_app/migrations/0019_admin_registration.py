# Generated by Django 4.1 on 2023-03-22 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0018_seller_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=50, unique=True)),
                ('password', models.TextField(max_length=50)),
            ],
        ),
    ]
