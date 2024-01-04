from django.shortcuts import render
from .models import Project

def index(request):
    return render(request, "portfolio/index.html",{
        "projects": Project.objects.all(),
        'estados':[cat[1] for cat in Project.STATUS_CHOICES],
    })