from django.urls import path

#from Pokemon.AppPrincipal.models import Ataque
from .views import registro

urlpatterns=[
    path('registro', registro, name='registrate')
]