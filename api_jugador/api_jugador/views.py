from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Personaje, Escena, Tiempo, Objeto, PersonajeObjeto
from .serializers import PersonajeSerializer, EscenaSerializer, TiempoSerializer, ObjetoSerializer, PersonajeObjetoSerializer

class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all()
    serializer_class = PersonajeSerializer
    
    def list(self, request, *args, **kwargs):
        personajes = self.get_queryset()
        serializer = self.get_serializer(personajes, many=True)
        return Response({
            "mensaje": "Lista de personajes obtenida con éxito",
            "cantidad": personajes.count(),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        personaje = self.get_object()
        serializer = self.get_serializer(personaje)
        return Response({
            "mensaje": "Detalles del personaje obtenidos correctamente",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Personaje creado exitosamente", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        personaje = self.get_object()
        serializer = self.get_serializer(personaje, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Personaje actualizado con éxito", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        personaje = self.get_object()
        personaje.delete()
        return Response({"mensaje": "Personaje eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

class EscenaViewSet(viewsets.ModelViewSet):
    queryset = Escena.objects.all()
    serializer_class = EscenaSerializer
    
    def list(self, request, *args, **kwargs):
        Escena = self.get_queryset()
        serializer = self.get_serializer(Escena, many=True)
        return Response({
            "mensaje": "Lista de escenas obtenida con éxito",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        Escena = self.get_object()
        serializer = self.get_serializer(Escena)
        return Response({
            "mensaje": "Detalles de escenas obtenidos correctamente",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "escena creado exitosamente", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        Escena = self.get_object()
        serializer = self.get_serializer(Escena, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "escena actualizado con éxito", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        Escena = self.get_object()
        Escena.delete()
        return Response({"mensaje": "escena eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

class TiempoViewSet(viewsets.ModelViewSet):
    queryset = Tiempo.objects.all()
    serializer_class = TiempoSerializer
    
    def list(self, request, *args, **kwargs):
        Tiempo = self.get_queryset()
        serializer = self.get_serializer(Tiempo, many=True)
        return Response({
            "mensaje": "Lista de tiempos obtenida con éxito",
            "cantidad": Tiempo.count(),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        Tiempo = self.get_object()
        serializer = self.get_serializer(Tiempo)
        return Response({
            "mensaje": "Detalles de tiempo obtenidos correctamente",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "tiempo registrado exitosamente", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        Tiempo = self.get_object()
        serializer = self.get_serializer(Tiempo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "tiempo actualizado con éxito", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        Tiempo = self.get_object()
        Tiempo.delete()
        return Response({"mensaje": "tiempo eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

class ObjetoViewSet(viewsets.ModelViewSet):
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer
    
    def list(self, request, *args, **kwargs):
        Objeto = self.get_queryset()
        serializer = self.get_serializer(Objeto, many=True)
        return Response({
            "mensaje": "Lista de objetos obtenida con éxito",
            "cantidad": Objeto.count(),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        Objeto = self.get_object()
        serializer = self.get_serializer(Objeto)
        return Response({
            "mensaje": "Detalles del objeto obtenidos correctamente",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "objeto creado exitosamente", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        Objeto = self.get_object()
        serializer = self.get_serializer(Objeto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "objeto actualizado con éxito", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        Objeto = self.get_object()
        Objeto.delete()
        return Response({"mensaje": "objeto eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

class PersonajeObjetoViewSet(viewsets.ModelViewSet):
    queryset = PersonajeObjeto.objects.all()
    serializer_class = PersonajeObjetoSerializer
    
    def list(self, request, *args, **kwargs):
        PersonajeObjeto = self.get_queryset()
        serializer = self.get_serializer(PersonajeObjeto, many=True)
        return Response({
            "mensaje": "Lista de relaciones obtenida con éxito",
            "cantidad": PersonajeObjeto.count(),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        PersonajeObjeto = self.get_object()
        serializer = self.get_serializer(PersonajeObjeto)
        return Response({
            "mensaje": "detalles del relación obtenidos correctamente",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "relación creado exitosamente", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        PersonajeObjeto = self.get_object()
        serializer = self.get_serializer(PersonajeObjeto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "relación actualizado con éxito", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        PersonajeObjeto = self.get_object()
        PersonajeObjeto.delete()
        return Response({"mensaje": "relación eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)

# Create your views here.
