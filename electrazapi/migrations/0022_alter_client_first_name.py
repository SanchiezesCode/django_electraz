# Generated by Django 5.0.3 on 2024-05-15 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrazapi', '0021_alter_client_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]