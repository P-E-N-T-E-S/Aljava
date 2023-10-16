from django.urls import path, include
from . import views

urlpatterns =[
    path("", views.home, name="home"),
    path("login", views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path("add_projeto",views.add_projeto, name="add_projeto"),
    path("add_dados",views.add_dados, name="add_dados"),
    path("add_linhas/<str:dado_impacto_id>",views.add_linhas, name="add_linhas"),
    path("visualizar_projetos",views.visualizar_projetos, name="visualizar_projetos"),
    path("editar_linha_impacto/<str:dado_impacto_id>",views.editar_linha_impacto, name="editar_linha_impacto"),
    path("detalhes_dado/<str:dado_impacto_id>",views.visualizar_linhas_impacto, name="detalhes_dado"),
]