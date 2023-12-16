from django.forms import Form, CharField, EmailField, PasswordInput, ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from tarefas.models import Tarefa


class FormNovoUsuario(Form):
    nome_do_usuario = CharField()
    nome = CharField(required=False)
    email = EmailField(required=False, max_length=255, help_text="e.g., user@example.com")
    senha = CharField(widget=PasswordInput)
    confirmacao_senha = CharField(widget=PasswordInput)

    # Criação do método para incluir a classe "form-control" em todos os elementos do formulário
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def save(self):
        params = {
            'username': self.cleaned_data['nome_do_usuario'],
            'email': self.cleaned_data['email'],
            'password': self.cleaned_data['senha']
        }
        if self.cleaned_data['nome']:
            params['first_name'] = self.cleaned_data['nome']
        User.objects.create_user(**params)

    def clean_confirmacao_senha(self):
        senha1 = self.cleaned_data['senha']
        senha2 = self.cleaned_data['confirmacao_senha']

        if senha1 != senha2:
            raise ValidationError("As senhas devem ser iguais.")

        return senha1

class FormTarefa(ModelForm):

    # Criação do método para incluir a classe "form-control" em todos os elementos do formulário
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['descricao'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao', 'status']