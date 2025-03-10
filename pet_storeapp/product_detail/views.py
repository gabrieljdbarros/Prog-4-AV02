from django.shortcuts import render
from django.conf import settings

PRODUTOS = [
    {"id": 1, "nome": "Ração Premium", "descricao": "Ração de alta qualidade para cães.", "preco": "99,90", "imagem": "https://m.media-amazon.com/images/I/610Y7nUpo3L._AC_UF1000,1000_QL80_.jpg"},
    {"id": 2, "nome": "Arranhador para Gatos", "descricao": "Arranhador resistente para gatos brincarem.", "preco": "120,00", "imagem": "https://gattedo.com.br/wp-content/uploads/2020/04/comprar-arranhador-para-gatos-torre-gattedo.jpg"},
    {"id": 3, "nome": "Coleira Personalizada", "descricao": "Coleira ajustável e confortável.", "preco": "30,00", "imagem": "https://blog-static.petlove.com.br/wp-content/uploads/2019/12/gato-coleira-petlove.jpg"},
    {"id": 4, "nome": "Brinquedo Mordedor", "descricao": "Brinquedo de borracha resistente para cães.", "preco": "25,00", "imagem": "https://www.petmimos.com.br/cdn/shop/products/brinquedo-mordedor-com-bola-para-cachorro-434117.jpg?v=1717017595"},
    {"id": 5, "nome": "James", "descricao": "James.", "preco": "2000,00", "imagem": "https://preview.redd.it/oqpv2kg43bge1.jpeg?auto=webp&s=2d62601ea50adf1c196bb19b45fa70a659c50bd8"},
    {"id": 6, "nome": "Larry", "descricao": "Larry.", "preco": "4500,00", "imagem": "https://preview.redd.it/evil-larry-contender-v0-o2vtj7gpkb6e1.jpeg?width=1170&format=pjpg&auto=webp&s=10958a5cea725761891c1c5037d0da4617c1376d"},
]

def product_detail(request, produto_id):
    produto_id = int(produto_id)
    produto = next((p for p in PRODUTOS if p["id"] == produto_id), None)

    if not produto:
        return render(request, "product_detail/not_found.html")

    return render(request, "product_detail/product_detail.html", {"produto": produto})
