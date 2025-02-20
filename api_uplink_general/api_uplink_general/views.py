from rest_framework import viewsets, status
from rest_framework import response
from .models import Historia, TiempoMapas, Mapas, Empresas, Ciberataque, PuntosDefensa, EmpresasPuntoDefensa

from .serializer import HistoriaSerializer, TiempoMapasSerializer, MapasSerializer, EmpresasSerializer, CiberataqueSerializer, PuntosDefensaSerializer, EmpresasPuntoDefensaSerializer


class HistoriaViewSet(viewsets.ModelViewSet):
    queryset = Historia.objects.all()
    serializer_class = HistoriaSerializer



class TiempoMapasViewSet(viewsets.ModelViewSet):
    queryset = TiempoMapas.objects.all()
    serializer_class = TiempoMapasSerializer

class MapasViewSet(viewsets.ModelViewSet):
    queryset = Mapas.objects.all()
    serializer_class = MapasSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer


class CiberataqueViewSet(viewsets.ModelViewSet):
    queryset = Ciberataque.objects.all()
    serializer_class = CiberataqueSerializer

class PuntosDefensaViewSet(viewsets.ModelViewSet):
    queryset = PuntosDefensa.objects.all()
    serializer_class = PuntosDefensaSerializer

class EmpresasPuntoDefensaViewSet(viewsets.ModelViewSet):
    queryset = EmpresasPuntoDefensa.objects.all()
    serializer_class = EmpresasPuntoDefensaSerializer