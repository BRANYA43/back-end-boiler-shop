# Generated by Django 4.2.7 on 2024-02-15 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('utils', '0001_initial'),
        ('products', '0003_productimageset_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimageset',
            name='cover_image',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='_image_set',
                to='utils.image',
                verbose_name='Cover Image',
            ),
        ),
    ]
