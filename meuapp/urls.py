from django.urls import path
from meuapp import views

urlpatterns = [
     path('', views.menu),
     path('menu/', views.menu),
     path('colaborador/', views.colaborador, name= "colaborador"),
     path('cadastrar/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
     path('cadastrar_equipamento/', views.cadastrar_equipamento, name='cadastrar_equipamento'),
     # Outra URL para página de sucesso
     path('sucesso/', views.sucesso, name='sucesso'),
     path('equipamento/sucesso/', views.sucesso_equipamento, name='sucesso_equipamento'),

     
]