# Generated by Django 4.1.5 on 2024-01-05 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_skill_project_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='skills/documents/')),
            ],
        ),
        migrations.RemoveField(
            model_name='skill',
            name='document',
        ),
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.ImageField(blank=True, upload_to='skills/images/'),
        ),
        migrations.AddField(
            model_name='skill',
            name='certificates',
            field=models.ManyToManyField(blank=True, to='portfolio.certificate'),
        ),
    ]
