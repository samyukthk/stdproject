# Generated by Django 3.2.25 on 2024-04-24 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stdapp', '0002_rename_university_school'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='School',
            new_name='University',
        ),
    ]
