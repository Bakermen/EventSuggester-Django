# Generated by Django 4.2.3 on 2023-07-10 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventcountry',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='flights',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='weather',
            old_name='event_id',
            new_name='event',
        ),
    ]
