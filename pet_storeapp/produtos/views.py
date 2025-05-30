from django.views.generic import TemplateView, ListView, DetailView, FormView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Produto, Servico, Agendamento

class ProdutosHomeView(TemplateView):
    template_name = 'produtos/home.html'

class ListaProdutoView(ListView):
    model = Produto
    template_name = 'produtos/list_product.html'
    context_object_name = 'produtos'

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produtos/product_detail.html'
    context_object_name = 'produto'
    pk_url_kwarg = 'produto_id'

class CadastroUsuarioView(FormView):
    template_name = 'produtos/cadastro.html'
    form_class = UserCreationForm
    success_url = '/produtos/login/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Usuário criado com sucesso! Faça login.')
        return super().form_valid(form)

class LoginUsuarioView(LoginView):
    template_name = 'produtos/login.html'

class LogoutUsuarioView(LogoutView):
    next_page = '/produtos/login/'

class ListaServicosView(LoginRequiredMixin, ListView):
    model = Servico
    template_name = 'produtos/lista_servicos.html'
    context_object_name = 'servicos'

class AgendarServicoView(LoginRequiredMixin, View):
    def get(self, request, servico_id):
        servico = Servico.objects.get(id=servico_id)
        return render(request, 'produtos/agendar_servico.html', {'servico': servico})

    def post(self, request, servico_id):
        servico = Servico.objects.get(id=servico_id)
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

class MinhasReservasView(LoginRequiredMixin, ListView):
    template_name = 'produtos/minhas_reservas.html'
    context_object_name = 'agendamentos'

    def get_queryset(self):
        return Agendamento.objects.filter(usuario=self.request.user).order_by('data_agendada')