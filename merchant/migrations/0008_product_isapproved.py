# Generated by Django 4.1 on 2023-04-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0007_product_productserving'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='isApproved',
            field=models.BooleanField(default='False'),
        ),
    ]