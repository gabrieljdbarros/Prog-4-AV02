from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Produto
from .models import Servico, Agendamento
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


#PRODUTOS = [
 #   {"id": 1, "nome": "Ração Premium", "descricao": "Ração de alta qualidade para cães.", "preco": "99,90", "imagem": "https://m.media-amazon.com/images/I/610Y7nUpo3L._AC_UF1000,1000_QL80_.jpg"},
 #   {"id": 2, "nome": "Arranhador para Gatos", "descricao": "Arranhador para gatos.", "preco": "120,00", "imagem": "https://gattedo.com.br/wp-content/uploads/2020/04/comprar-arranhador-para-gatos-torre-gattedo.jpg"},
  #  {"id": 3, "nome": "Coleira Personalizada", "descricao": "Coleira ajustável.", "preco": "30,00", "imagem": "https://blog-static.petlove.com.br/wp-content/uploads/2019/12/gato-coleira-petlove.jpg"},
   ###{"id": 5, "nome": "James", "descricao": "James.", "preco": "2000,00", "imagem": "https://preview.redd.it/oqpv2kg43bge1.jpeg?auto=webp&s=2d62601ea50adf1c196bb19b45fa70a659c50bd8"},
    #{"id": 6, "nome": "Larry", "descricao": "Larry.", "preco": "4500,00", "imagem": "https://preview.redd.it/evil-larry-contender-v0-o2vtj7gpkb6e1.jpeg?width=1170&format=pjpg&auto=webp&s=10958a5cea725761891c1c5037d0da4617c1376d"},
#]

def home(request):
    return render(request, 'produtos/home.html')



def list_product(request):
    produtos = Produto.objects.all()
    return render(request, "produtos/list_product.html", {"produtos": produtos})




def product_detail(request, produto_id):
    produtos = get_object_or_404(Produto, id=produto_id)
    return render(request, "produtos/product_detail.html", {"produto": produtos})







def cadastro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso! Faça login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'produtos/cadastro.html', {'form': form})





def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_produtos')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'produtos/login.html')

@login_required
def logout_usuario(request):
    logout(request)
    return redirect('login')


@login_required
def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'produtos/lista_servicos.html', {'servicos': servicos})

@login_required
def agendar_servico(request, servico_id):
    servico = Servico.objects.get(id=servico_id)
    if request.method == 'POST':
        data = request.POST.get('data_agendada')
        horario = request.POST.get('horario')
        obs = request.POST.get('observacoes', '')
        Agendamento.objects.create(
            usuario=request.user,
            servico=servico,
            data_agendada=data,
            horario=horario,
            observacoes=obs
        )
        messages.success(request, 'Serviço agendado com sucesso!')
        return redirect('minhas_reservas')
    return render(request, 'produtos/agendar_servico.html', {'servico': servico})

@login_required
def minhas_reservas(request):
    agendamentos = Agendamento.objects.filter(usuario=request.user).order_by('data_agendada')
    return render(request, 'produtos/minhas_reservas.html', {'agendamentos': agendamentos})
