# Generated by Django 3.2.16 on 2022-11-26 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plots', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plot',
            old_name='req_id',
            new_name='reqid',
        ),
    ]
