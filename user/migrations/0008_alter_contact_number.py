# Generated by Django 4.1 on 2023-05-02 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.IntegerField(),
        ),
    ]
