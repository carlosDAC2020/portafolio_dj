from django.db import models
from datetime import date


class Project(models.Model):
    STATUS_CHOICES = [
        ('Desarrollando', 'Desarrollando'),
        ('Terminado', 'Terminado'),
        ('Pendiente', 'Pendiente'),  
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='en_proceso')
    image = models.ImageField(upload_to="portfolio/", blank=True)
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title


