# Generated by Django 4.2.3 on 2024-02-05 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0010_alter_fin_sales_order_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fin_Recurring_invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Email', models.CharField(blank=True, max_length=20, null=True)),
                ('Customer_Billing_Address', models.CharField(blank=True, max_length=20, null=True)),
                ('Customer_GST_Type', models.CharField(blank=True, max_length=20, null=True)),
                ('Customer_GST_Number', models.CharField(blank=True, max_length=20, null=True)),
                ('Customer_Place_of_Supply', models.CharField(blank=True, max_length=20, null=True)),
                ('Entry_Type', models.CharField(blank=True, max_length=20, null=True)),
                ('Profile_Name', models.CharField(blank=True, max_length=20, null=True)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('Reference_Number', models.CharField(blank=True, max_length=20, null=True)),
                ('Order_Number', models.IntegerField()),
                ('Repeat_Every', models.CharField(blank=True, max_length=20, null=True)),
                ('Payment_Method', models.CharField(blank=True, max_length=20, null=True)),
                ('Cheque_Number', models.CharField(blank=True, max_length=20, null=True)),
                ('UPI_Number', models.CharField(blank=True, max_length=20, null=True)),
                ('Bank_Account_Number', models.CharField(blank=True, max_length=20, null=True)),
                ('Description', models.CharField(blank=True, max_length=20, null=True)),
                ('Document', models.ImageField(blank=True, null=True, upload_to='image/RCIN')),
                ('Sub_Total', models.IntegerField()),
                ('CGST', models.IntegerField()),
                ('SGST', models.IntegerField()),
                ('Tax_Amount', models.IntegerField()),
                ('IGST', models.IntegerField()),
                ('Shipping_charge', models.IntegerField()),
                ('Adjustment', models.IntegerField()),
                ('Grand_Total', models.IntegerField()),
                ('Status', models.CharField(blank=True, max_length=20, null=True)),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('LoginDetails', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('Payment_Terms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_payment_terms')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_customers')),
            ],
        ),
        migrations.AddField(
            model_name='fin_sales_order',
            name='converted_to_rec_invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finsys_App.fin_recurring_invoice'),
        ),
    ]
