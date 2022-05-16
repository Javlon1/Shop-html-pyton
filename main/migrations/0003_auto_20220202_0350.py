# Generated by Django 3.2.9 on 2022-02-01 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_new_arrivals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='image')),
                ('name', models.CharField(max_length=255)),
                ('narx', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Featured_Product',
        ),
    ]