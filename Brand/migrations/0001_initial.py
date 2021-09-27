# Generated by Django 3.2.2 on 2021-05-08 10:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MediaCollection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('brandId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('Sports Shop', 'Sports Shop'), ('Car', 'Car'), ('Energy Drinks', 'Energy Drinks'), ('Clothing', 'Clothing')], max_length=50)),
                ('websiteLink', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('advertisementCollections', models.OneToOneField(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brand_advertisement', to='MediaCollection.mediacollection')),
                ('logoCollections', models.OneToOneField(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brand_logo', to='MediaCollection.mediacollection')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
