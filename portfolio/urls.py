from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index,  name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('proyect_detail/<int:project_id>/', views.project_detail, name='project_detail'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('superuser/', views.create_superuser),
]