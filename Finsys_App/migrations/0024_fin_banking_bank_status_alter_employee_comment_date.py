# Generated by Django 4.2.3 on 2024-03-01 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0023_fin_purchase_order_alter_employee_comment_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fin_banking',
            name='bank_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employee_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 1)),
        ),
    ]
