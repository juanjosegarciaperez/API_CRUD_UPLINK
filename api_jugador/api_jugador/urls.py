from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonajeViewSet, EscenaViewSet, TiempoViewSet, ObjetoViewSet, PersonajeObjetoViewSet

router = DefaultRouter()
router.register(r'personaje', PersonajeViewSet)
router.register(r'escena', EscenaViewSet)
router.register(r'tiempo', TiempoViewSet)
router.register(r'objeto', ObjetoViewSet)
router.register(r'personaje-objeto', PersonajeObjetoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
