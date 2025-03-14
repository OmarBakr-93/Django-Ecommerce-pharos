from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('blogs/', include('blogs.urls')),
    path('store/', include('store.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
