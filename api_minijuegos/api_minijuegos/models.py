from django.db import models

class Recompensa(models.Model):
    id_recompensa = models.AutoField(primary_key=True)
    valor_recompensa = models.CharField(max_length=255)
    id_personaje = models.IntegerField()  # Suponiendo que se relaciona con otra tabla
    id_reputacion = models.IntegerField()  # Suponiendo que se relaciona con otra tabla
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Recompensa {self.id_recompensa} - {self.valor_recompensa}"


class Minijuego(models.Model):
    id_minijuegos = models.AutoField(primary_key=True)
    nombre_minijuego = models.CharField(max_length=255)
    descripcion_minijuego = models.TextField()
    id_recompensa = models.ForeignKey(Recompensa, on_delete=models.SET_NULL, null=True, blank=True)
    id_tiempo_minijuegos = models.IntegerField()  # Relación con tiempo_minijuegos
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_minijuego


class TiempoMinijuego(models.Model):
    id_tiempo_minijuegos = models.AutoField(primary_key=True)
    tiempo_minijuegos = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tiempo: {self.tiempo_minijuegos}"

# Create your models here.
