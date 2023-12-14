from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('communication/', include('communication.urls', namespace='conversation')),
    path('stripe_integration/', include('stripe_integration.urls')),
    path('items/', include('item.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
