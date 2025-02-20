from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Historia, TiempoMapas, Mapas, Empresas, Ciberataque, PuntosDefensa, EmpresasPuntoDefensa

from .serializer import HistoriaSerializer, TiempoMapasSerializer, MapasSerializer, EmpresasSerializer, CiberataqueSerializer, PuntosDefensaSerializer, EmpresasPuntoDefensaSerializer


class BaseViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registro creado exitosamente", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": "Error al crear el registro", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registro actualizado correctamente", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"error": "Error al actualizar el registro", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Registro eliminado exitosamente"}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"message": "Detalles del registro", "data": serializer.data}, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"message": "Lista de registros", "data": serializer.data}, status=status.HTTP_200_OK)

# Vistas específicas para cada modelo
class MapasViewSet(BaseViewSet):
    queryset = Mapas.objects.all()
    serializer_class = MapasSerializer

class TiempoMapasViewSet(BaseViewSet):
    queryset = TiempoMapas.objects.all()
    serializer_class = TiempoMapasSerializer

class EmpresasViewSet(BaseViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer

class HistoriaViewSet(BaseViewSet):
    queryset = Historia.objects.all()
    serializer_class = HistoriaSerializer


class CiberataqueViewSet(BaseViewSet):
    queryset = Ciberataque.objects.all()
    serializer_class = CiberataqueSerializer

class PuntosDefensaViewSet(BaseViewSet):
    queryset = PuntosDefensa.objects.all()
    serializer_class = PuntosDefensaSerializer

class EmpresasPuntoDefensaViewSet(BaseViewSet):
    queryset = EmpresasPuntoDefensa.objects.all()
    serializer_class = EmpresasPuntoDefensaSerializer