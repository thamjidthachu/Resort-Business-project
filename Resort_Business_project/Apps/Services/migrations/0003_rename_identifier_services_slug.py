# Generated by Django 4.0.3 on 2022-04-19 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_alter_services_identifier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='identifier',
            new_name='slug',
        ),
    ]
