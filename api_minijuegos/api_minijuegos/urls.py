from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecompensaViewSet, MinijuegoViewSet, TiempoMinijuegoViewSet

router = DefaultRouter()
router.register(r'recompensa', RecompensaViewSet)
router.register(r'minijuego', MinijuegoViewSet)
router.register(r'tiempos-minijuego', TiempoMinijuegoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
