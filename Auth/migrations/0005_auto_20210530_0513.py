# Generated by Django 3.2.2 on 2021-05-30 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0004_alter_user_ismoderator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='primaryEmailVerified',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='primaryPhoneVerified',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
