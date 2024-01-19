# Generated by Django 4.2.3 on 2024-01-19 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0002_fin_invoice_fin_invoice_reference_fin_invoice_items_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fin_Vendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, null=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('website', models.CharField(max_length=100, null=True)),
                ('gst_type', models.CharField(max_length=100, null=True)),
                ('gstin', models.CharField(max_length=100, null=True)),
                ('pan_no', models.CharField(max_length=100, null=True)),
                ('opening_balance', models.FloatField(blank=True, default=0.0, null=True)),
                ('open_balance_type', models.CharField(blank=True, max_length=100, null=True)),
                ('current_balance', models.FloatField(blank=True, default=0.0, null=True)),
                ('credit_limit', models.FloatField(blank=True, default=0.0, null=True)),
                ('place_of_supply', models.CharField(blank=True, max_length=100, null=True)),
                ('currency', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('billing_street', models.CharField(max_length=100, null=True)),
                ('billing_city', models.CharField(max_length=100, null=True)),
                ('billing_state', models.CharField(max_length=100, null=True)),
                ('billing_pincode', models.CharField(max_length=100, null=True)),
                ('billing_country', models.CharField(max_length=100, null=True)),
                ('ship_street', models.CharField(max_length=100, null=True)),
                ('ship_city', models.CharField(max_length=100, null=True)),
                ('ship_state', models.CharField(max_length=100, null=True)),
                ('ship_pincode', models.CharField(max_length=100, null=True)),
                ('ship_country', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(default='Active', max_length=15)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('LoginDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('payment_terms', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finsys_App.fin_company_payment_terms')),
                ('price_list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finsys_App.fin_price_list')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Vendor_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('action', models.CharField(blank=True, choices=[('Created', 'Created'), ('Edited', 'Edited')], max_length=20, null=True)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('LoginDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('Vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_vendors')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Vendor_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=500, null=True)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('Vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_vendors')),
            ],
        ),
    ]
