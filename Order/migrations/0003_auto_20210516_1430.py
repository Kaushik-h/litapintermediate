# Generated by Django 3.2.2 on 2021-05-16 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproducts',
            name='GiftBioId',
        ),
        migrations.RemoveField(
            model_name='orderproducts',
            name='dimension',
        ),
        migrations.RemoveField(
            model_name='orderproducts',
            name='firstLocation',
        ),
        migrations.RemoveField(
            model_name='orderproducts',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderproducts',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderProducts',
        ),
    ]