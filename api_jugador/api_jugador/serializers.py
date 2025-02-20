from rest_framework import serializers
from .models import Personaje, Escena, Tiempo, Objeto, PersonajeObjeto

class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = '__all__'

class EscenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escena
        fields = '__all__'

class TiempoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiempo
        fields = '__all__'

class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto
        fields = '__all__'

class PersonajeObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonajeObjeto
        fields = '__all__'