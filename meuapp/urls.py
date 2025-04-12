from django.urls import path
from meuapp import views

urlpatterns = [
     path('', views.menu),
     path('menu/', views.menu),
     path('colaborador/', views.colaborador, name= "colaborador"),
     path('cadastrar/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
     # Outra URL para página de sucesso
     path('sucesso/', views.sucesso, name='sucesso'),
]