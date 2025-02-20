from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HistoriaViewSet, TiempoMapasViewSet, MapasViewSet, EmpresasViewSet, CiberataqueViewSet, PuntosDefensaViewSet, EmpresasPuntoDefensaViewSet



router = DefaultRouter()
router.register(r'historias', HistoriaViewSet)
router.register(r'tiempos-mapas', TiempoMapasViewSet)
router.register(r'mapas', MapasViewSet)
router.register(r'empresas', EmpresasViewSet)
router.register(r'ciberataques', CiberataqueViewSet)
router.register(r'puntos-defensa', PuntosDefensaViewSet)
router.register(r'empresas-puntos-defensa', EmpresasPuntoDefensaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]