# Generated by Django 4.1.5 on 2024-01-14 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0024_rename_url_project_url_deploy_project_summary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='my_cv',
            field=models.FileField(blank=True, upload_to='profile/cv/'),
        ),
    ]
