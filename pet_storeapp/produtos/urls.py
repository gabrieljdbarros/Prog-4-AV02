from django.urls import path
from .views import (
    ProdutosHomeView,
    ListaProdutoView,
    CadastroUsuarioView,
    LoginUsuarioView,
    LogoutUsuarioView,
    ListaServicosView,
    AgendarServicoView,
    MinhasReservasView,
    ProdutoDetailView
)

urlpatterns = [
    path('home/', ProdutosHomeView.as_view(), name='produtos_home'),
    path('list_product/', ListaProdutoView.as_view(), name='list_product'),
    path('cadastro/', CadastroUsuarioView.as_view(), name='cadastro'),
    path('login/', LoginUsuarioView.as_view(), name='login'),
    path('logout/', LogoutUsuarioView.as_view(), name='logout'),
    path('servicos/', ListaServicosView.as_view(), name='lista_servicos'),
    path('servicos/<int:servico_id>/agendar/', AgendarServicoView.as_view(), name='agendar_servico'),
    path('minhas-reservas/', MinhasReservasView.as_view(), name='minhas_reservas'),
    path('produto/<int:produto_id>/', ProdutoDetailView.as_view(), name='product_detail'),
]