# Generated by Django 3.1.5 on 2021-04-07 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210122_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo_user',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
