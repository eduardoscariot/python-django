from django.shortcuts import render, redirect
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from django.views.generic import View
from tarefas.models import Tarefa
from tarefas.forms import FormNovoUsuario, FormTarefa


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


class CriarUsuario(View):
    template_name = 'tarefas/criar_usuario.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = FormNovoUsuario()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = FormNovoUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)


class CriarTarefa(View):
    template_name = 'tarefas/criar_tarefa.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = FormTarefa()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = FormTarefa(request.POST)
        print(request.user)
        if form.is_valid():
            #form['usuario'] = request.user
            form.save()
            return redirect('/tarefas/')
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)
