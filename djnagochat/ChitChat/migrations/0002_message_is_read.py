# Generated by Django 4.2.16 on 2024-09-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChitChat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
