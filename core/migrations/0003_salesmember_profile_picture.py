# Generated by Django 5.0.6 on 2024-05-31 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_salesmember_lead'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesmember',
            name='profile_picture',
            field=models.ImageField(default='profile_pictures/default.jpg', upload_to='profile_pictures'),
        ),
    ]
