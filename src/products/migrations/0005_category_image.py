# Generated by Django 4.2.7 on 2024-01-22 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('utils', '0001_initial'),
        ('products', '0004_remove_product_price_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='categories',
                to='utils.image',
            ),
        ),
    ]
