# Generated by Django 3.2.5 on 2022-11-15 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_attendance_is_present'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='is_present',
            field=models.BooleanField(default=False),
        ),
    ]
