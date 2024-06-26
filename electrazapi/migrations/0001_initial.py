# Generated by Django 5.0.3 on 2024-05-17 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, unique=True)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='поставщик')),
                ('link', models.URLField(blank=True, default='', verbose_name='сайт')),
            ],
            options={
                'verbose_name': 'поставщик',
                'verbose_name_plural': 'поставщики',
            },
        ),
        migrations.CreateModel(
            name='ManufacturerProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='производитель')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electrazapi.country', verbose_name='страна')),
            ],
            options={
                'verbose_name': 'производитель',
                'verbose_name_plural': 'производители',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(blank=True, decimal_places=0, max_digits=7, null=True)),
                ('old_price', models.DecimalField(blank=True, decimal_places=0, max_digits=7, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('additional_info', models.TextField(blank=True)),
                ('meta_tag', models.CharField(blank=True, max_length=100)),
                ('meta_description', models.CharField(blank=True, max_length=200)),
                ('meta_keywords', models.CharField(blank=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('photo', models.ImageField(blank=True, upload_to='products/')),
                ('is_available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='electrazapi.categoryproduct')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='electrazapi.manufacturerproduct')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=0, max_digits=7)),
                ('link', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electrazapi.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electrazapi.supplier')),
            ],
            options={
                'unique_together': {('product', 'supplier')},
            },
        ),
    ]
