# Generated by Django 4.1.5 on 2023-01-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listings_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='image',
            field=models.ImageField(blank=True, default='Photo', upload_to='auctions/files/images'),
        ),
    ]
