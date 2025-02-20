from django.db import models

# Create your models here.

class Historia(models.Model):
    capitulo = models.IntegerField()
    titulo_capitulo = models.CharField(max_length=255)
    contenido_capitulo = models.TextField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    


class TiempoMapas(models.Model):
    odo_noche = models.BooleanField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    

class Mapas(models.Model):
    nombre_mapas = models.CharField(max_length=255)
    historia = models.ForeignKey(Historia, on_delete=models.CASCADE)
    tiempo = models.ForeignKey(TiempoMapas, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    


class Empresas(models.Model):
    nombre_empresa = models.CharField(max_length=255)
    ciberataque = models.ForeignKey('Ciberataque', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    


class Ciberataque(models.Model):
    resultado = models.CharField(max_length=255)
    minijuegos = models.IntegerField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    


class PuntosDefensa(models.Model):
    personaje_id = models.IntegerField()
    estado = models.CharField(max_length=255)
    ultimo_ataque = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    

class EmpresasPuntoDefensa(models.Model):
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    punto_defensa = models.ForeignKey(PuntosDefensa, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)