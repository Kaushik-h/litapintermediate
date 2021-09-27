# Generated by Django 3.2.2 on 2021-05-16 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MediaCollection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KYC',
            fields=[
                ('kycId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('kycStatus', models.CharField(choices=[('NotStarted', 'NotStarted'), ('Incomplete', 'Incomplete'), ('CompeletedSuccessful', 'CompeletedSuccessful'), ('Expired', 'Expired')], max_length=20)),
                ('kycDate', models.DateTimeField()),
                ('country', models.CharField(max_length=20)),
                ('identityId', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('identityType', models.CharField(blank=True, choices=[('Passport', 'Passport'), ('NationalId', 'NationalId'), ('License', 'License')], default=None, max_length=20, null=True)),
                ('verificationType', models.CharField(choices=[('BANK', 'BANK'), ('LITAP', 'LITAP')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tribe',
            fields=[
                ('tribeId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('bio', models.TextField()),
                ('tribeDescription', models.TextField()),
                ('fans', models.ManyToManyField(blank=True, related_name='tribes', to=settings.AUTH_USER_MODEL)),
                ('moderator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tribeModerator', to=settings.AUTH_USER_MODEL)),
                ('tribeLeader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('bioId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('age', models.PositiveIntegerField()),
                ('interests', models.CharField(max_length=100)),
                ('clubs', models.CharField(max_length=100)),
                ('records', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mediaCollection', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MediaCollection.mediacollection')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bio', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
