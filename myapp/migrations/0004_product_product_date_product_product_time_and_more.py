# Generated by Django 4.1.3 on 2022-12-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_venue',
            field=models.TextField(default=''),
        ),
    ]
