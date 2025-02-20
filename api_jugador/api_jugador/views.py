from rest_framework import viewsets
from .models import Personaje, Escena, Tiempo, Objeto, PersonajeObjeto
from .serializers import PersonajeSerializer, EscenaSerializer, TiempoSerializer, ObjetoSerializer, PersonajeObjetoSerializer

class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all()
    serializer_class = PersonajeSerializer

class EscenaViewSet(viewsets.ModelViewSet):
    queryset = Escena.objects.all()
    serializer_class = EscenaSerializer

class TiempoViewSet(viewsets.ModelViewSet):
    queryset = Tiempo.objects.all()
    serializer_class = TiempoSerializer

class ObjetoViewSet(viewsets.ModelViewSet):
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer

class PersonajeObjetoViewSet(viewsets.ModelViewSet):
    queryset = PersonajeObjeto.objects.all()
    serializer_class = PersonajeObjetoSerializer

# Create your views here.
