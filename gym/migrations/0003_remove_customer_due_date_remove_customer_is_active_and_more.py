# Generated by Django 5.0.6 on 2024-07-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_customer_due_date_customer_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='feedetail',
            name='duration_in_months',
        ),
        migrations.AddField(
            model_name='feedetail',
            name='month',
            field=models.PositiveSmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=7),
        ),
    ]