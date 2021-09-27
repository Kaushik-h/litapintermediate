# Generated by Django 3.2.2 on 2021-05-08 10:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhysicalLocation',
            fields=[
                ('addressId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('addressLine1', models.CharField(max_length=40)),
                ('addressLine2', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('zipcode', models.CharField(max_length=20)),
                ('mailCode', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
