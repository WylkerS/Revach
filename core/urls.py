from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from base.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto