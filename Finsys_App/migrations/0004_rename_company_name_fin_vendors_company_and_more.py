# Generated by Django 4.2.3 on 2024-01-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0003_fin_vendors_fin_vendor_history_fin_vendor_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fin_vendors',
            old_name='company_name',
            new_name='company',
        ),
        migrations.AddField(
            model_name='fin_vendors',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
