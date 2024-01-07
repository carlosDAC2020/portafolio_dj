from django.shortcuts import render
from .models import Project, Skill, Profile, Blog

def index(request):
    projects= list(Project.objects.all())
    elements_by_divicion=6
    aux = len(projects)/elements_by_divicion
    if aux > int(aux):
        subdiviciones=int(aux)+1
    else:
        subdiviciones=int(aux)
    projects_order = []
    for i in range(subdiviciones):
        aux_list=[]
        for x in range(elements_by_divicion):
            try:
                initial_element = projects[0]
                projects.pop(0)
                aux_list.append(initial_element)
            except IndexError:
                break
        projects_order.append(aux_list)

    
    return render(request, "portfolio/index.html",{
        'profile':Profile.objects.filter(first_name__icontains='Carlos', last_name__icontains='Agamez')[0],
        "projects": Project.objects.all(),
        'skills':Skill.objects.all(),
        'estados':[cat[1] for cat in Project.STATUS_CHOICES],
        "blogs": Blog.objects.all()
    })

