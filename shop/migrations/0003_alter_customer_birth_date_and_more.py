# Generated by Django 4.0 on 2021-12-15 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_customer_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='registration_date',
            field=models.DateField(),
        ),
    ]
