from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecompensaViewSet, MinijuegoViewSet, TiempoMinijuegoViewSet

router = DefaultRouter()
router.register(r'recompensas', RecompensaViewSet)
router.register(r'minijuegos', MinijuegoViewSet)
router.register(r'tiempos-minijuegos', TiempoMinijuegoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
