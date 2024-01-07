from django.db import models
from django.utils.html import mark_safe
from markdown import markdown

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="profile/images/", blank=True)
    description = models.TextField()
    degree = models.CharField(max_length=100)  
    email = models.EmailField()  
    phone = models.CharField(max_length=15)  
    city = models.CharField(max_length=100)  
    age = models.IntegerField()  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def formatted_description(self):
        return self.description.replace('\n', '<br>')

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="skills/documents/")

    def __str__(self) -> str:
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="skills/images/", blank=True)
    certificates = models.ManyToManyField(Certificate, blank=True)

    def __str__(self) -> str:
        return self.title

class Project(models.Model):
    """
    # Project
    modelo de registro de mis proyectos 
    el cual tiene los siguientes atributos
    - title : nombre del proyecto
    - description : breve descripcion de lo q es el proyecto
    - status : estao actual de desarrollo del proyecto
    - image : imagen representativa deel proyecto
    - url : url del repo del proyecto 
    """
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
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self) -> str:
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    image = models.ImageField(upload_to="blog/images/", blank=True)
    body_markdown = models.TextField()

    def body_as_html(self):
        return mark_safe(markdown(self.body_markdown))

    def __str__(self):
        return self.title
