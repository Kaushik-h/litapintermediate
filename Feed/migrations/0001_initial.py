# Generated by Django 3.2.2 on 2021-05-08 10:58

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
            name='Feed',
            fields=[
                ('feedId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('createTime', models.DateTimeField()),
                ('lastUpdatedTime', models.DateTimeField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('contentType', models.CharField(choices=[('Audio', 'Audio'), ('Video', 'Video'), ('Text', 'Text'), ('Mix', 'Mix')], max_length=20)),
                ('public', models.BooleanField()),
                ('shareOption', models.BooleanField()),
                ('mediaCollection', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='feed', to='MediaCollection.mediacollection')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]