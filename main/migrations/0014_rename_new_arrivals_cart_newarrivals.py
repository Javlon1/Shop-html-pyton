# Generated by Django 3.2.9 on 2022-02-06 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='new_arrivals',
            new_name='newarrivals',
        ),
    ]
