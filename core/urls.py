from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from base.views import home_page, transactions_page, categories_page
from base.htmx_views import transactions_create, transactions_tipo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('transactions/', transactions_page, name='transactions'),
    path('categories/', categories_page, name='categories'),
]

htmx_urlpatterns = [
    path('create-transaction/', transactions_create, name="create_transaction"),
    path('transactions-tipo/', transactions_tipo, name="transactions_tipo"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto
urlpatterns += htmx_urlpatterns