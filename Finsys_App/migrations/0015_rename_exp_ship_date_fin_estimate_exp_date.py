# Generated by Django 4.2.3 on 2024-02-14 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0014_fin_estimate_bank_acc_no_fin_estimate_cheque_no_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fin_estimate',
            old_name='exp_ship_date',
            new_name='exp_date',
        ),
    ]
