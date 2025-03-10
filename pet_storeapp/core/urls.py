
from django.contrib import admin
from django.urls import path
from home.views import home_view
from list_product.views import list_product
from product_detail.views import product_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name="home"),
    path('list_product/', list_product, name="list_product"),
    path('product_detail/<int:produto_id>/', product_detail, name="product_detail"),
      
]