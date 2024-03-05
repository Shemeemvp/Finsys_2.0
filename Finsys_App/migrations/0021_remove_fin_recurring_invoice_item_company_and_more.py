# Generated by Django 4.2.3 on 2024-02-22 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0020_alter_employee_comment_date_fin_companyrepeatevery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fin_recurring_invoice_item',
            name='Company',
        ),
        migrations.RemoveField(
            model_name='fin_recurring_invoice_item',
            name='items',
        ),
        migrations.RemoveField(
            model_name='fin_recurring_invoice_item',
            name='recinvoice',
        ),
        migrations.RemoveField(
            model_name='fin_recurring_invoice_reference',
            name='Company',
        ),
        migrations.RemoveField(
            model_name='fin_estimate',
            name='converted_to_rec_invoice',
        ),
        migrations.RemoveField(
            model_name='fin_sales_order',
            name='converted_to_rec_invoice',
        ),
        migrations.DeleteModel(
            name='Fin_Recurring_invoice',
        ),
        migrations.DeleteModel(
            name='Fin_Recurring_invoice_item',
        ),
        migrations.DeleteModel(
            name='Fin_Recurring_Invoice_Reference',
        ),
    ]