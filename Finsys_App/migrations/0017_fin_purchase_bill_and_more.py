# Generated by Django 4.2.3 on 2024-02-16 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0016_fin_estimate_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fin_Purchase_Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.CharField(blank=True, max_length=100, null=True)),
                ('ref_no', models.IntegerField(blank=True, null=True)),
                ('porder_no', models.IntegerField(blank=True, null=True)),
                ('bill_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('pay_type', models.CharField(blank=True, max_length=100, null=True)),
                ('cheque_no', models.CharField(blank=True, max_length=100, null=True)),
                ('upi_no', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_no', models.CharField(blank=True, max_length=100, null=True)),
                ('ven_psupply', models.CharField(blank=True, max_length=100, null=True)),
                ('cust_psupply', models.CharField(blank=True, max_length=100, null=True)),
                ('subtotal', models.CharField(default=0, max_length=100, null=True)),
                ('igst', models.CharField(default=0, max_length=100, null=True)),
                ('cgst', models.CharField(default=0, max_length=100, null=True)),
                ('sgst', models.CharField(default=0, max_length=100, null=True)),
                ('taxamount', models.CharField(default=0, max_length=100, null=True)),
                ('ship_charge', models.CharField(default=0, max_length=100, null=True)),
                ('adjust', models.CharField(default=0, max_length=100, null=True)),
                ('grandtotal', models.FloatField(default=0, null=True)),
                ('paid', models.CharField(blank=True, max_length=255, null=True)),
                ('balance', models.CharField(blank=True, max_length=255, null=True)),
                ('file', models.FileField(upload_to='purchase_bill')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Save', 'Save')], default='Draft', max_length=10)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_customers')),
                ('logindetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('pay_term', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finsys_App.fin_company_payment_terms')),
                ('pricelist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_price_list')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_vendors')),
            ],
        ),
        migrations.RenameField(
            model_name='fin_recurring_invoice',
            old_name='Entity_Type',
            new_name='Entry_Type',
        ),
        migrations.AddField(
            model_name='fin_recurring_invoice',
            name='Price_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_price_list'),
        ),
        migrations.AddField(
            model_name='fin_recurring_invoice',
            name='recinvoiceno',
            field=models.CharField(default='RI00', max_length=100),
        ),
        migrations.CreateModel(
            name='Fin_Recurring_Invoice_Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_no', models.BigIntegerField()),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Purchase_Bill_Ref_No',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_no', models.CharField(default=0, max_length=100, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('logindetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Purchase_Bill_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0, null=True)),
                ('price', models.CharField(default=0, max_length=100, null=True)),
                ('tax', models.CharField(default=0, max_length=100, null=True)),
                ('discount', models.CharField(default=0, max_length=100, null=True)),
                ('total', models.IntegerField(default=0, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_items')),
                ('pbill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_purchase_bill')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Purchase_Bill_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateField(auto_now_add=True, null=True)),
                ('action', models.CharField(choices=[('Created', 'Created'), ('Updated', 'Updated')], max_length=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('logindetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('pbill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_purchase_bill')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Purchase_Bill_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default=0, max_length=100, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('logindetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('pbill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_purchase_bill')),
            ],
        ),
        migrations.AlterField(
            model_name='fin_recurring_invoice',
            name='Reference_Number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_recurring_invoice_reference'),
        ),
    ]
