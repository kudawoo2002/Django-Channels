# Generated by Django 5.0.4 on 2024-05-11 22:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_user_channel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Channel',
            new_name='UserChannel',
        ),
    ]
