# Generated by Django 3.2.2 on 2021-05-16 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MediaCollection', '0001_initial'),
        ('Brand', '0002_auto_20210508_1254'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('commodityId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=40)),
                ('commodityType', models.CharField(choices=[('Ball', 'Ball'), ('Bat', 'Bat'), ('Guards', 'Guards'), ('Studs', 'Studs'), ('Jersey', 'Jersey'), ('Shorts', 'Shorts'), ('Cap', 'Cap'), ('Image', 'Image')], max_length=20)),
                ('description', models.TextField()),
                ('rating', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('isDisabled', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomizationType',
            fields=[
                ('customizationTypeId', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('Signature', 'Signature'), ('Message', 'Message')], max_length=20)),
                ('value', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('productId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=40)),
                ('productType', models.CharField(choices=[('Ball', 'Ball'), ('Bat', 'Bat'), ('Guards', 'Guards'), ('Studs', 'Studs'), ('Jersey', 'Jersey'), ('Shorts', 'Shorts'), ('Cap', 'Cap'), ('Image', 'Image')], max_length=20)),
                ('description', models.TextField()),
                ('rating', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('isDisabled', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Brand.brand')),
                ('customizationType', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_customization', to='Product.customizationtype')),
                ('mediaCollection', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MediaCollection.mediacollection')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('dimensionId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('size', models.CharField(blank=True, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11')], default=None, max_length=10, null=True)),
                ('color', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('count', models.IntegerField(blank=True, default=None, null=True)),
                ('length', models.IntegerField(blank=True, default=None, null=True)),
                ('width', models.IntegerField(blank=True, default=None, null=True)),
                ('height', models.IntegerField(blank=True, default=None, null=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('lastUpdatedOrder', models.DateTimeField(blank=True, default=None, null=True)),
                ('lastUpdatedUser', models.DateTimeField(blank=True, default=None, null=True)),
                ('lastUpdatedTime', models.DateTimeField(blank=True, default=None, null=True)),
                ('commodity', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commodity_dimension', to='Product.commodity')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_dimension', to='Product.product')),
            ],
        ),
        migrations.AddConstraint(
            model_name='customizationtype',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('type__exact', 'Signature'), ('value__isnull', True)), models.Q(('type__exact', 'Message'), ('value__isnull', False)), _connector='OR'), name='customization_type_signature_must_be_null_value'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='brand',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commodities', to='Brand.brand'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='customizationType',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commodity_customization', to='Product.customizationtype'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='mediaCollection',
            field=models.OneToOneField(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MediaCollection.mediacollection'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
