from django.contrib import admin
from django.urls import path, include
from tarefas.views import Home, TarefasView, TarefaDetail, CriarUsuario, CriarTarefa

urlpatterns = [
    path('', Home.as_view()),
    path('tarefas/', TarefasView.as_view()),
    path('tarefas/criar/', CriarTarefa.as_view()),
    path('tarefas/<pk>/', TarefaDetail.as_view()),
    path('criar_usuario/', CriarUsuario.as_view()),
]
