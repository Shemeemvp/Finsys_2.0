# Generated by Django 4.2.3 on 2024-01-29 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0005_fin_banking'),
    ]

    operations = [
        migrations.AddField(
            model_name='fin_cnotification',
            name='Vendors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_vendors'),
        ),
    ]
