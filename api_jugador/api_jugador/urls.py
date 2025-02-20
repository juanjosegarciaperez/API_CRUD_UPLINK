from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonajeViewSet, EscenaViewSet, TiempoViewSet, ObjetoViewSet, PersonajeObjetoViewSet

router = DefaultRouter()
router.register(r'personajes', PersonajeViewSet)
router.register(r'escenas', EscenaViewSet)
router.register(r'tiempos', TiempoViewSet)
router.register(r'objetos', ObjetoViewSet)
router.register(r'personaje-objetos', PersonajeObjetoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
