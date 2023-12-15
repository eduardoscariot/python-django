from django.shortcuts import render
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from django.views.generic import View
from tarefas.models import Tarefa

# Create your views here.
class TarefasView(ArchiveIndexView):
    model = Tarefa
    date_field = 'data_de_criacao'

class TarefaDetail(DetailView):
    model = Tarefa

class Home(View):
    template_name = 'tarefas/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['counter'] = Tarefa.objects.filter(status=False).count()
        return render(request, self.template_name, self.context)