from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_carrinho, name='ver_carrinho'),
    path('adicionar-produto/<int:produto_id>/', views.add_produto_carrinho, name='add_produto_carrinho'),
    path('adicionar-servico/<int:servico_id>/', views.add_servico_carrinho, name='add_servico_carrinho'),
    path('remover/<str:item_id>/<str:tipo>/', views.remover_item_carrinho, name='remover_item_carrinho'),
]