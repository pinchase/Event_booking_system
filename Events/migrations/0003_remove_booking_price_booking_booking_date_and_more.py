# Generated by Django 5.0.2 on 2024-11-30 22:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_booking_price_event_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='price',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=django.utils.timezone.now, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='number_of_tickets',
            field=models.PositiveIntegerField(),
        ),
    ]