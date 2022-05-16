# Generated by Django 3.2.9 on 2022-02-01 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('number', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('work_day', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('work_day', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Featured_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='image')),
                ('img2', models.ImageField(upload_to='image')),
                ('img3', models.ImageField(upload_to='image')),
                ('img4', models.ImageField(upload_to='image')),
                ('name', models.CharField(max_length=255)),
                ('catergory_name', models.CharField(max_length=255)),
                ('narx', models.IntegerField()),
                ('reting', models.IntegerField()),
                ('discriptions', models.TextField()),
                ('productId', models.IntegerField()),
                ('delivery', models.CharField(max_length=255)),
            ],
        ),
    ]