# Generated by Django 3.2.2 on 2021-05-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0007_remove_orderproducts_giftreason'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproducts',
            name='giftReason',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
