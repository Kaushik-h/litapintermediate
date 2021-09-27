# Generated by Django 3.2.2 on 2021-05-16 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MediaCollection', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('InProgress', 'InProgress'), ('PendingDocumentVerification', 'PendingDocumentVerification'), ('PendingIdentityVerification', 'PendingIdentityVerification'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('approvedBy', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('collectionId', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MediaCollection.mediacollection')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='leader_request', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
