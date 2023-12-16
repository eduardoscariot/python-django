from django.db.models import Model, deletion
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import TextField
from django.db.models import ForeignKey
from django.contrib.auth.models import User


# Create your models here.
class Tarefa(Model):
    data_de_criacao = DateTimeField(auto_now_add=True, verbose_name='data de criação')
    data_de_execucao = DateTimeField(verbose_name='data de execução', null=True)
    nome = CharField(max_length=200, verbose_name='nome')
    descricao = TextField(verbose_name='descrição', null=True, blank=True)
    status = BooleanField(default=False, verbose_name='finalizado')
    usuario = ForeignKey(User, verbose_name="usuário", null=True, blank=True, on_delete=deletion.PROTECT)

    class Meta:
        ordering = ['-data_de_criacao']
