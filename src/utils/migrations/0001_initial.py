# Generated by Django 4.2.7 on 2024-02-11 19:48

from django.db import migrations, models
import utils.utils
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies: list = []

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Title')),
                ('value', models.CharField(max_length=50, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Attribute',
                'verbose_name_plural': 'Attributes',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Title')),
                ('image', models.ImageField(upload_to=utils.utils.get_upload_filename, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
