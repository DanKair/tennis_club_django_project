# Generated by Django 5.1.6 on 2025-02-22 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='player_age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='player_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='player_first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='player_last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='playermanager',
            old_name='player_manager_name',
            new_name='manager_name',
        ),
    ]
