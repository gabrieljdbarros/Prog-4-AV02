from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import HomeView
import debug_toolbar

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('produtos/', include('produtos.urls')),
    path('carrinho/', include('carrinho.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)