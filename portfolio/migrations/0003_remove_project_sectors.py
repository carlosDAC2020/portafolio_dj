# Generated by Django 4.1.5 on 2023-01-15 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_sector_technology_project_sectors_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='sectors',
        ),
    ]
