from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('list_product/', views.list_product, name='list_product'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('servicos/', views.lista_servicos, name='lista_servicos'),
    path('servicos/<int:servico_id>/agendar/', views.agendar_servico, name='agendar_servico'),
    path('minhas-reservas/', views.minhas_reservas, name='minhas_reservas'),
    path('produto/<int:produto_id>/', views.product_detail, name='product_detail'),
]