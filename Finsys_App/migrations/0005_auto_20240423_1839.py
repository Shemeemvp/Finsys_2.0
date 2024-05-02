# Generated by Django 3.2.25 on 2024-04-23 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0004_auto_20240420_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='fin_creditnote_items',
            name='sac',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='fin_debit_note_items',
            name='sac',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='fin_delivery_challan_items',
            name='sac',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='fin_estimate_items',
            name='sac',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fin_eway_items',
            name='sac',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fin_invoice_items',
            name='sac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fin_purchase_order_items',
            name='sac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fin_recurring_bill_items',
            name='sac',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fin_recurring_invoice_items',
            name='sac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fin_retainer_invoice_items',
            name='SAC',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fin_sales_order_items',
            name='sac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 4, 23)),
        ),
        migrations.AlterField(
            model_name='fin_attendance_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 4, 23)),
        ),
        migrations.AlterField(
            model_name='fin_attendance_history',
            name='date',
            field=models.DateField(default=datetime.date(2024, 4, 23)),
        ),
        migrations.AlterField(
            model_name='fin_estimate_items',
            name='hsn',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fin_retainer_invoice',
            name='Customer_billing_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fin_retainer_invoice',
            name='Customer_gst_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='holiday_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 4, 23)),
        ),
    ]