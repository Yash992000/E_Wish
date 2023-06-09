# Generated by Django 4.1 on 2023-04-26 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('categoryId', models.AutoField(primary_key=True, serialize=False)),
                ('categoryName', models.TextField(blank=True, max_length=50, unique=True)),
                ('categoryImage', models.ImageField(blank=True, null=True, upload_to='administrator/image')),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('dietId', models.AutoField(primary_key=True, serialize=False)),
                ('dietType', models.TextField(blank=True, max_length=50, unique=True)),
                ('dietDisc', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Categories',
            fields=[
                ('subcategoryId', models.AutoField(primary_key=True, serialize=False)),
                ('subcategoryName', models.TextField(blank=True, max_length=50, unique=True)),
                ('subcategoryImage', models.ImageField(blank=True, null=True, upload_to='administrator/image')),
                ('categoryName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='administrator.categories')),
            ],
        ),
    ]
