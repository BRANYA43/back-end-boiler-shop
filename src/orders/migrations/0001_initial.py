# Generated by Django 4.2.7 on 2024-02-11 19:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import orders.models
import orders.validators
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                (
                    'delivery',
                    models.CharField(
                        choices=[('pickup', 'Pickup'), ('nova_post', 'Nova post')],
                        default='pickup',
                        max_length=50,
                        verbose_name='Delivery Way',
                    ),
                ),
                (
                    'delivery_address',
                    models.CharField(blank=True, max_length=255, null=True, verbose_name='Delivery Address'),
                ),
                (
                    'payment',
                    models.CharField(
                        choices=[
                            ('visa', 'Visa'),
                            ('mastercard', 'Mastercard'),
                            ('cash_on_delivery', 'Cash on delivery'),
                        ],
                        default='cash_on_delivery',
                        max_length=50,
                        verbose_name='Payment',
                    ),
                ),
                ('is_paid', models.BooleanField(default=False, verbose_name='Is Paid')),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('in_processing', 'In processing'),
                            ('completed', 'Completed'),
                            ('canceled', 'Canceled'),
                        ],
                        default='in_processing',
                        max_length=50,
                        verbose_name='Status',
                    ),
                ),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                (
                    'quantity',
                    models.PositiveIntegerField(
                        default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Quantity'
                    ),
                ),
                (
                    'order',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='products',
                        to='orders.order',
                        verbose_name='Order',
                    ),
                ),
                (
                    'price',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='order_products',
                        to='products.price',
                        verbose_name='Price',
                    ),
                ),
                (
                    'product',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='order_products',
                        to='products.product',
                        verbose_name='Product',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Order Product',
                'verbose_name_plural': 'Order Products',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                (
                    'full_name',
                    models.CharField(
                        max_length=100,
                        validators=[django.core.validators.MinLengthValidator(3), orders.validators.validate_name],
                        verbose_name='Full Name',
                    ),
                ),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', orders.models.PhoneField(max_length=50, verbose_name='Phone')),
                (
                    'order',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='customer',
                        to='orders.order',
                        verbose_name='Order',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
