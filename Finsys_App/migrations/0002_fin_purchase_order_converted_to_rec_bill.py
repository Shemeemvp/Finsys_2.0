# Generated by Django 4.2.3 on 2024-05-02 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fin_purchase_order',
            name='converted_to_rec_bill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finsys_App.fin_recurring_bills'),
        ),
    ]
