# Generated by Django 4.2.3 on 2024-01-24 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0004_rename_company_name_fin_vendors_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fin_Banking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(blank=True, max_length=255, null=True)),
                ('account_number', models.CharField(blank=True, max_length=255, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=255, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=255, null=True)),
                ('opening_balance_type', models.CharField(blank=True, max_length=255, null=True)),
                ('opening_balance', models.IntegerField(default=0, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('current_balance', models.IntegerField(default=0, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
            ],
        ),
    ]