# Generated by Django 4.2.7 on 2024-01-16 10:58

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies: list = []

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
