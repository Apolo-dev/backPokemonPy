from django.urls import path, include

#from Pokemon.AppPrincipal.models import Ataque
from .views import FantasmaViewset, HieloViewset, LuchaViewset, DragonViewset, FuegoViewset, PsiquicoViewset, TierraViewset, AguaViewset, ElectricoViewset, VoladorViewset, LegendarioViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('dragon', DragonViewset)
router.register('fuego', FuegoViewset)
router.register('tierra', TierraViewset)
router.register('agua', AguaViewset)
router.register('electrico', ElectricoViewset)
router.register('hielo', HieloViewset)
router.register('psiquico', PsiquicoViewset)
router.register('lucha', LuchaViewset)
router.register('fantasma', FantasmaViewset)
router.register('volador', VoladorViewset)
router.register('legendario', LegendarioViewset)




urlpatterns=[
    
    #path con django rest framework
    path('', include(router.urls)),
]