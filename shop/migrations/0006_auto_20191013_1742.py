# Generated by Django 2.2.4 on 2019-10-13 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20191013_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Laptops', 'Laptops'), ('Desktops', 'Desktops'), ('Tablets', 'Tablets'), ('Gaming', 'Gaming'), ('Workstation', 'Workstation'), ('Servers & Storage', 'Servers & Storage'), ('Networking', 'Networking'), ('Monitors', 'Monitors'), ('Electronics & Accessories', 'Electronics & Accessories')], db_index=True, help_text='Enter category name of product', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(choices=[('Laptops', 'Laptops'), ('Desktops', 'Desktops'), ('Tablets', 'Tablets'), ('Gaming', 'Gaming'), ('Workstation', 'Workstation'), ('Servers & Storage', 'Servers & Storage'), ('Networking', 'Networking'), ('Monitors', 'Monitors'), ('Electronics & Accessories', 'Electronics & Accessories')], on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Category'),
        ),
    ]
