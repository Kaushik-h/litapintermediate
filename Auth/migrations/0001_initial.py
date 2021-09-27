# Generated by Django 3.2.2 on 2021-05-08 06:59

import Auth.models
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('userId', models.CharField(default=uuid.uuid4, editable=False, max_length=250, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=12, unique=True)),
                ('firstName', models.CharField(max_length=20)),
                ('middleName', models.CharField(default=None, max_length=20, null=True)),
                ('lastName', models.CharField(max_length=20)),
                ('isTribeLeader', models.BooleanField(blank=True, default=None, null=True)),
                ('isModerator', models.BooleanField(blank=True, default=None, null=True)),
                ('primaryPhone', models.CharField(blank=True, default=None, max_length=20, null=True, unique=True)),
                ('primaryEmail', models.EmailField(blank=True, default=None, max_length=254, null=True, unique=True)),
                ('primaryPhoneVerified', models.BooleanField(blank=True, default=None, null=True)),
                ('primaryEmailVerified', models.BooleanField(blank=True, default=None, null=True)),
                ('followers', models.ManyToManyField(blank=True, related_name='followee', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CallbackToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('key', models.CharField(default=Auth.models.RandomKeyGenerator, max_length=128, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('primaryPhone__isnull', True), ('primaryEmail__isnull', True)), _negated=True), name='primaryEmail_primaryPhone_not_both_null'),
        ),
        migrations.AddIndex(
            model_name='callbacktoken',
            index=models.Index(fields=['user'], name='Auth_callba_user_id_509c3a_idx'),
        ),
    ]