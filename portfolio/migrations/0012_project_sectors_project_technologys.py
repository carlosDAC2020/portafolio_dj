# Generated by Django 4.1.5 on 2023-01-15 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_remove_sector_imege_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='sectors',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.sector'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='technologys',
            field=models.ManyToManyField(to='portfolio.technology'),
        ),
    ]
