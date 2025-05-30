from django.shortcuts import redirect, render, get_object_or_404
from produtos.models import Produto, Servico
from django.contrib import messages

def inicializa_carrinho(sessao):
    if 'carrinho' not in sessao:
        sessao['carrinho'] = {'produtos': {}, 'servicos': {}}
    sessao.modified = True

def add_produto_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    inicializa_carrinho(request.session)
    carrinho = request.session['carrinho']

    item = carrinho['produtos'].get(str(produto.id), {
        'nome': produto.nome,
        'preco': float(produto.preco),
        'quantidade': 0
    })
    item['quantidade'] += 1
    carrinho['produtos'][str(produto.id)] = item
    request.session.modified = True
    messages.success(request, f"{produto.nome} adicionado ao carrinho.")
    return redirect('list_product')

def add_servico_carrinho(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    inicializa_carrinho(request.session)
    carrinho = request.session['carrinho']
    carrinho['servicos'][str(servico.id)] = {
        'nome': servico.nome,
        'preco': float(servico.preco)
    }
    request.session.modified = True
    messages.success(request, f"Serviço '{servico.nome}' adicionado ao carrinho.")
    return redirect('lista_servicos')

def ver_carrinho(request):
    inicializa_carrinho(request.session)
    carrinho = request.session['carrinho']

    total = 0

    
    for item in carrinho['produtos'].values():
        total += item['preco'] * item['quantidade']

    
    for item in carrinho['servicos'].values():
        total += item['preco']

    return render(request, 'produtos/carrinho.html', {
        'carrinho': carrinho,
        'total': total
    })

def remover_item_carrinho(request, item_id, tipo):
    inicializa_carrinho(request.session)
    if tipo in ['produtos', 'servicos'] and item_id in request.session['carrinho'][tipo]:
        del request.session['carrinho'][tipo][item_id]
        request.session.modified = True
        messages.info(request, "Item removido do carrinho.")
    return redirect('ver_carrinho')