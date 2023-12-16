from django.test import TestCase
from django.test import Client
from django.db.utils import IntegrityError
from tarefas.models import Tarefa


# Create your tests here.
class TesteDummy(TestCase):
    def test_true(self):
        self.assertTrue(True)


class CriarTarefaTestCase(TestCase):
    def test_cria_tarefa_vazia(self):
        self.assertIsNotNone(Tarefa.objects.create())

    def test_cria_tarefa_sem_nome(self):
        with self.assertRaises(IntegrityError):
            Tarefa.objects.create(nome=None)

    def test_cria_tarefa_com_nome(self):
        self.assertIsNotNone(Tarefa.objects.create(nome="Teste tarefa"))


class HomeTestCase(TestCase):
    def test_home_access(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Olá')

    def test_home_tem_link_login(self):
        response = self.client.get('/')
        if response.context['user'].is_authenticated:
            self.assertNotContains(response, "Login")
        else:
            self.assertContains(response, "Login")
