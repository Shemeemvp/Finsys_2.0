# Generated by Django 3.2.25 on 2024-04-18 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fin_CreditNote1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('billing_address', models.TextField(blank=True, null=True)),
                ('gst_type', models.CharField(blank=True, max_length=100, null=True)),
                ('gstin', models.CharField(blank=True, max_length=100, null=True)),
                ('place_of_supply', models.CharField(blank=True, max_length=100, null=True)),
                ('creditnote_number', models.CharField(blank=True, max_length=100)),
                ('creditnote_date', models.DateField(blank=True, null=True)),
                ('reference_number', models.IntegerField(blank=True, null=True)),
                ('invoice_number', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_type', models.CharField(blank=True, max_length=100, null=True)),
                ('price_list_applied', models.BooleanField(default=False, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=100, null=True)),
                ('cheque_number', models.CharField(blank=True, max_length=100, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_account', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('document', models.FileField(blank=True, upload_to='file/')),
                ('subtotal', models.IntegerField(default=0, null=True)),
                ('igst', models.FloatField(blank=True, default=0.0, null=True)),
                ('cgst', models.FloatField(blank=True, default=0.0, null=True)),
                ('sgst', models.FloatField(blank=True, default=0.0, null=True)),
                ('tax_amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('adjustment', models.FloatField(blank=True, default=0.0, null=True)),
                ('shipping_charge', models.FloatField(blank=True, default=0.0, null=True)),
                ('grandtotal', models.FloatField(blank=True, default=0.0, null=True)),
                ('paid', models.IntegerField(default=0, null=True)),
                ('balance', models.FloatField(blank=True, default=0.0, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('status', models.CharField(default='Draft', max_length=150)),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('Customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_customers')),
                ('LoginDetails', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('price_list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finsys_App.fin_price_list')),
            ],
        ),
    ]