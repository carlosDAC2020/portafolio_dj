from django.shortcuts import render, get_object_or_404
from .models import Project, Skill, Profile, Blog

def index(request): 
    return render(request, "portfolio/index.html",{
        'profile':Profile.objects.filter(first_name__icontains='Carlos', last_name__icontains='Agamez')[0],
        "projects": Project.objects.filter(is_important=True),
        'skills':Skill.objects.all(),
        'estados':[cat[1] for cat in Project.STATUS_CHOICES],
        "blogs": Blog.objects.all()
    })

def portfolio(request):
    return render(request, "portfolio/portfolio.html",{
        'projects':Project.objects.all(),
        'estados':[cat[1] for cat in Project.STATUS_CHOICES]
    })

def project_detail(request, project_id):
    
    project = get_object_or_404(Project, id=project_id)
    
    print(project)
    return render(request, 'portfolio/proyect_detail.html', {
        'project':project,
        'skills': project.skills.all(),
    })

def blog(request):
    return render(request,'portfolio/blog.html', {
        'blogs':Blog.objects.all(),
    })

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'portfolio/blog_detail.html', {
        'blog':blog,
    })