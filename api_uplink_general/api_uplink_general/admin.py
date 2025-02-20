from django.contrib import admin
from .models import Historia, TiempoMapas, Mapas, Empresas, Ciberataque, PuntosDefensa, EmpresasPuntoDefensa

# Register your models here.

admin.site.register(Historia)
admin.site.register(TiempoMapas)
admin.site.register(Mapas)
admin.site.register(Empresas)
admin.site.register(Ciberataque)
admin.site.register(PuntosDefensa)
admin.site.register(EmpresasPuntoDefensa)