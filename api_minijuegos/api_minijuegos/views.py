from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Recompensa, Minijuego, TiempoMinijuego
from .serializers import RecompensaSerializer, MinijuegoSerializer, TiempoMinijuegoSerializer

class RecompensaViewSet(viewsets.ModelViewSet):
    queryset = Recompensa.objects.all()
    serializer_class = RecompensaSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': 'Recompensa creada exitosamente',
            'data': response.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            'message': 'Recompensa actualizada correctamente',
            'data': response.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({
            'message': 'Recompensa eliminada con éxito'
        }, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response({
            'message': 'Detalles de la recompensa obtenidos',
            'data': response.data
        }, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'message': 'Lista de recompensas obtenida',
            'data': response.data
        }, status=status.HTTP_200_OK)

class MinijuegoViewSet(viewsets.ModelViewSet):
    queryset = Minijuego.objects.all()
    serializer_class = MinijuegoSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': 'Minijuego creado exitosamente',
            'data': response.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            'message': 'Minijuego actualizado correctamente',
            'data': response.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({
            'message': 'Minijuego eliminado con éxito'
        }, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response({
            'message': 'Detalles del minijuego obtenidos',
            'data': response.data
        }, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'message': 'Lista de minijuegos obtenida',
            'data': response.data
        }, status=status.HTTP_200_OK)

class TiempoMinijuegoViewSet(viewsets.ModelViewSet):
    queryset = TiempoMinijuego.objects.all()
    serializer_class = TiempoMinijuegoSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': 'Tiempo de minijuego registrado exitosamente',
            'data': response.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            'message': 'Tiempo de minijuego actualizado correctamente',
            'data': response.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({
            'message': 'Tiempo de minijuego eliminado con éxito'
        }, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response({
            'message': 'Detalles del tiempo de minijuego obtenidos',
            'data': response.data
        }, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'message': 'Lista de tiempos de minijuegos obtenida',
            'data': response.data
        }, status=status.HTTP_200_OK)



# Create your views here.
