# Generated by Django 4.2.7 on 2024-01-07 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_delete_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='image',
            field=models.ImageField(default='C:/Users/OMEN 16/Desktop/django/commerce/auctions/media/images/test.avif', upload_to='images/'),
        ),
    ]