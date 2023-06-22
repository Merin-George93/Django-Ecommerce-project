# Generated by Django 4.2 on 2023-06-06 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_account_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='totalprice',
            new_name='no_ofitems',
        ),
        migrations.AlterField(
            model_name='order',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(default='Pending', max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='Pending', max_length=30),
        ),
    ]
