
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# para el login
from AppUser.login import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('AppPrincipal.urls')),
    path('api/', include('AppUser.urls')),
    path('',Login.as_view(), name = 'login')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)