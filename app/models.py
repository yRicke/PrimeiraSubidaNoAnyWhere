from django.db import models

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)

    @classmethod
    def adicionarContato(cls, nome, telefone):
        return cls.objects.create(nome=nome, telefone = telefone)

    @classmethod
    def deletarContato(cls, id):
        cls.objects.filter(id=id).delete()
    
    @classmethod
    def listarContatos(cls):
        return cls.objects.all()

    def __str__(self):
        return self.nome