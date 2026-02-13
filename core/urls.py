from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from base.views import home_page, transactions_page, categories_page, create_transaction
from base.htmx_views import delete_transaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('transactions/', transactions_page, name='transactions'),
    path('categories/', categories_page, name='categories'),
    path('transactions/create/', create_transaction, name="create_transaction")
]

htmx_urlpatterns = [
    path('transactions/delete/<pk>/', delete_transaction, name='delete_transaction'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto
urlpatterns += htmx_urlpatterns