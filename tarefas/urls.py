from django.contrib import admin
from django.urls import path, include
from tarefas.views import Home, TarefasView, TarefaDetail

urlpatterns = [
    path('', Home.as_view()),
    path('tarefas/', TarefasView.as_view()),
    path('tarefas/<pk>/', TarefaDetail.as_view()),
]
