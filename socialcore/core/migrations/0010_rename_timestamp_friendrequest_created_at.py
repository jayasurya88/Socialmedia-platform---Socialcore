# Generated by Django 5.1.1 on 2024-10-05 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_friendrequest_friendship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendrequest',
            old_name='timestamp',
            new_name='created_at',
        ),
    ]
