# Generated by Django 3.2.2 on 2021-05-16 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0004_leaderrequest'),
        ('Location', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0007_auto_20210516_1138'),
        ('Order', '0003_auto_20210516_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('orderDate', models.DateTimeField()),
                ('deliveryDate', models.DateTimeField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('orderStatus', models.CharField(choices=[('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('RefundInitiated', 'RefundInitiated'), ('RefundComplete', 'RefundComplete')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deliveryAddress', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='Location.physicallocation')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('orderProductId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('deliveryType', models.CharField(choices=[('Express', 'Express'), ('OneDay', 'OneDay'), ('Priority', 'Priority')], max_length=20)),
                ('isDelivered', models.BooleanField(default=False)),
                ('deliveryDate', models.DateTimeField()),
                ('orderStatus', models.CharField(choices=[('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('RefundInitiated', 'RefundInitiated'), ('RefundComplete', 'RefundComplete')], max_length=20)),
                ('giftReason', models.TextField(blank=True, default=None, null=True)),
                ('GiftBioId', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Profile.bio')),
                ('dimension', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.dimension')),
                ('firstLocation', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Location.physicallocation')),
                ('order', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='productObjects', to='Order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderObjects', to='Product.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='orderProducts',
            field=models.ManyToManyField(related_name='orders', through='Order.OrderProducts', to='Product.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]