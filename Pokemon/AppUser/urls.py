from django.urls import path

#from Pokemon.AppPrincipal.models import Ataque
from .views import  Registrar

urlpatterns=[
    path('registrar/', Registrar.as_view(), name='registrarse'),
]