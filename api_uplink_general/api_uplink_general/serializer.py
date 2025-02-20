
from rest_framework import serializers
from .models import Historia, Empresas, PuntosDefensa, EmpresasPuntoDefensa, Mapas, TiempoMapas, Ciberataque

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = '__all__'

class PuntosDefensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuntosDefensa
        fields = '__all__'

class EmpresasPuntoDefensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresasPuntoDefensa
        fields = '__all__'

class MapasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapas
        fields = '__all__'

class TiempoMapasSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiempoMapas
        fields = '__all__'

class CiberataqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciberataque
        fields = '__all__'