# Generated by Django 5.0.3 on 2024-05-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrazapi', '0017_alter_supplier_options_alter_client_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
    ]