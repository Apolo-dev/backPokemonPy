
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# para el login
from AppUser.login import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('AppPrincipal.urls')),
    path('api/', include('AppUser.urls')),
    path('',Login.as_view(), name = 'login'),
    path('logout/',Logout.as_view(), name = 'Logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)