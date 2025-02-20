from django.db import models

# Tabla Personaje
class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    tiempo_juego = models.DurationField()  # Se cambió TimeField() a DurationField()
    minijuegos_jugados = models.IntegerField()
    minijuegos_perdidos = models.IntegerField()
    minijuegos_ganados = models.IntegerField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre

# Tabla Escena
class Escena(models.Model):
    posicion_x = models.FloatField()
    posicion_y = models.FloatField()
    ubi_minijuego = models.IntegerField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

# Tabla Tiempo
class Tiempo(models.Model):
    tiempo_juego = models.TimeField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE, related_name="tiempos")

# Tabla Objeto
class Objeto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

# Tabla Intermedia: Personaje_Objeto
class PersonajeObjeto(models.Model):
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE, related_name="objetos")
    objeto = models.ForeignKey(Objeto, on_delete=models.CASCADE, related_name="personajes")
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)