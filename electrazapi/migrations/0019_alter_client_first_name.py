# Generated by Django 5.0.3 on 2024-05-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrazapi', '0018_alter_client_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]