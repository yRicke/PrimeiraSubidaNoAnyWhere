from django.shortcuts import render, redirect
from app.models import Contato

# Create your views here.

def novoContato(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        telefone = request.POST.get("telefone")
        Contato.adicionarContato(nome, telefone)
        return redirect("index")
    return redirect("index")


def index(request):
    return render(request, 'index.html', {"contatos":Contato.listarContatos()})

def deletarContato(request, id):
    Contato.deletarContato(id)
    return redirect('index')