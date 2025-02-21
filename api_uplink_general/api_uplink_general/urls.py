from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HistoriaViewSet, TiempoMapasViewSet, MapasViewSet, EmpresasViewSet, CiberataqueViewSet, PuntosDefensaViewSet, EmpresasPuntoDefensaViewSet



router = DefaultRouter()
router.register(r'historia', HistoriaViewSet)
router.register(r'tiempos-mapa', TiempoMapasViewSet)
router.register(r'mapa', MapasViewSet)
router.register(r'empresas', EmpresasViewSet)
router.register(r'ciberataque', CiberataqueViewSet)
router.register(r'puntos-defensa', PuntosDefensaViewSet)
router.register(r'empresas-puntos-defensa', EmpresasPuntoDefensaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]