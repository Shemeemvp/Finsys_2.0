# Generated by Django 4.2.3 on 2024-02-02 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0007_fin_invoice_price_list_applied'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fin_Sales_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('billing_address', models.TextField(blank=True, null=True)),
                ('gst_type', models.CharField(blank=True, max_length=100, null=True)),
                ('gstin', models.CharField(blank=True, max_length=100, null=True)),
                ('place_of_supply', models.CharField(blank=True, max_length=100, null=True)),
                ('reference_no', models.IntegerField(blank=True, null=True)),
                ('sales_order_no', models.CharField(max_length=100)),
                ('sales_order_date', models.DateField(blank=True, null=True)),
                ('exp_ship_date', models.DateField(blank=True, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=100, null=True)),
                ('cheque_no', models.CharField(blank=True, max_length=100, null=True)),
                ('upi_no', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_acc_no', models.CharField(blank=True, max_length=100, null=True)),
                ('subtotal', models.IntegerField(default=0, null=True)),
                ('igst', models.FloatField(blank=True, default=0.0, null=True)),
                ('cgst', models.FloatField(blank=True, default=0.0, null=True)),
                ('sgst', models.FloatField(blank=True, default=0.0, null=True)),
                ('tax_amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('adjustment', models.FloatField(blank=True, default=0.0, null=True)),
                ('shipping_charge', models.FloatField(blank=True, default=0.0, null=True)),
                ('grandtotal', models.FloatField(blank=True, default=0.0, null=True)),
                ('paid_off', models.FloatField(blank=True, default=0.0, null=True)),
                ('balance', models.FloatField(blank=True, default=0.0, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('file', models.FileField(default='default.jpg', upload_to='sales_order')),
                ('status', models.CharField(default='Draft', max_length=150)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('Customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_customers')),
                ('LoginDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('converted_to_invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finsys_App.fin_invoice')),
                ('payment_terms', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finsys_App.fin_company_payment_terms')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Sales_Order_Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_no', models.BigIntegerField()),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('LoginDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Sales_Order_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsn', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('price', models.FloatField(blank=True, default=0.0, null=True)),
                ('total', models.FloatField(blank=True, default=0.0, null=True)),
                ('tax', models.CharField(max_length=100, null=True)),
                ('discount', models.FloatField(blank=True, default=0.0, null=True)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('Item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finsys_App.fin_items')),
                ('LoginDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('SalesOrder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_sales_order')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Sales_Order_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('action', models.CharField(blank=True, choices=[('Created', 'Created'), ('Edited', 'Edited')], max_length=20, null=True)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('LoginDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('SalesOrder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_sales_order')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Sales_Order_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=500, null=True)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('SalesOrder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_sales_order')),
            ],
        ),
    ]
