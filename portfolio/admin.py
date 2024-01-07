

from django.contrib import admin
from .models import Project, Skill, Certificate, Profile, Blog

class SkillInline(admin.TabularInline):
    model = Project.skills.through  
    extra = 1

class CertificateInline(admin.TabularInline):
    model = Skill.certificates.through
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [SkillInline]
    filter_horizontal = ('skills',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    inlines = [CertificateInline]
    filter_horizontal = ('certificates',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile)

admin.site.register(Blog)
