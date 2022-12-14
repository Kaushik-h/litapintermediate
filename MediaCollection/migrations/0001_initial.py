# Generated by Django 3.2.2 on 2021-05-08 10:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaCollection',
            fields=[
                ('collectionId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('collectionType', models.CharField(choices=[('ProductMediaCollection', 'ProductMediaCollection'), ('LogoCollection', 'LogoCollection'), ('ReviewMediaCollection', 'ReviewMediaCollection'), ('BrandMediaCollection', 'BrandMediaCollection'), ('EventMediaCollection', 'EventMediaCollection')], max_length=30)),
                ('collectionSeverity', models.CharField(choices=[('Confidential', 'Confidential'), ('Public', 'Public'), ('Private', 'Private')], max_length=30)),
            ],
        ),
    ]
