# Generated by Django 5.0.3 on 2024-05-13 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrazapi', '0015_alter_productsupplier_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='asdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('url', models.URLField()),
            ],
        ),
    ]