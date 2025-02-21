from rest_framework import serializers
from .models import Recompensa, Minijuego, TiempoMinijuego

class RecompensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recompensa
        fields = '__all__'

class MinijuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minijuego
        fields = '__all__'

class TiempoMinijuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiempoMinijuego
        fields = '__all__'
