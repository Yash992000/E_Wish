# Generated by Django 4.1 on 2023-05-01 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
        ('user', '0004_remove_cartitems_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('BillId', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('total_price', models.IntegerField()),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='BillItems',
            fields=[
                ('BillItemId', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('productQty', models.IntegerField()),
                ('Bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.bill')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.cart')),
            ],
        ),
    ]
