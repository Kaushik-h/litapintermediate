# Generated by Django 3.2.2 on 2021-05-16 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Endorsement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endorsementrequest',
            old_name='collectionId',
            new_name='collection',
        ),
    ]
