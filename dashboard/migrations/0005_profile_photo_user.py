# Generated by Django 3.1.5 on 2021-04-07 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_profile_photo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo_user',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]