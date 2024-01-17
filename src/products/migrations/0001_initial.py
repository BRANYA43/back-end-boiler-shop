# Generated by Django 4.2.7 on 2024-01-17 09:12

import uuid

import django.db.models.deletion
from django.db import migrations, models

import products.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                (
                    'parent',
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='sub_categories',
                        to='products.category',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    'stock',
                    models.CharField(
                        choices=[('in_stock', 'In stock'), ('out_of_stock', 'Out of stock'), ('to_order', 'To order')],
                        default='in_stock',
                        max_length=20,
                    ),
                ),
                ('description', models.TextField(blank=True, null=True)),
                ('is_displayed', models.BooleanField(default=True)),
                ('grade', models.JSONField(default=products.models._set_grade_dict)),
                (
                    'category',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.category'
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('attributes', models.ManyToManyField(related_name='specifications', to='utils.attribute')),
                (
                    'product',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='products.product'
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
