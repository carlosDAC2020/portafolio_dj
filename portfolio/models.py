from django.db import models
from datetime import date


class Project(models.Model):
    STATUS_CHOICES = [
        ('en_proceso', 'En Proceso'),
        ('terminado', 'Terminado'),
        ('pendiente', 'Pendiente'),  # Puedes agregar más estados según tus necesidades
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='en_proceso')
    image = models.ImageField(upload_to="portfolio/images")
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title


