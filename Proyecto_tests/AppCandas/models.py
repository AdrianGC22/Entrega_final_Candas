from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Moto(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    estado = models.CharField(max_length=20)
    año = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return f"Marca: {self.marca} Modelo: {self.modelo}" 
    
class Sucursal(models.Model):
    provincia = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    direccion = models.CharField(max_length=20)
    telefono = models.IntegerField()

    def __str__(self):
        return f"Provincia: {self.provincia} Localidad: {self.localidad}" 
    
    
    
    
    
class Avatar(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares" , null=True , blank=True)

    def __str__(self):
        return f"User: {self.user}  -  Imagen: {self.imagen}"
    
class Repuesto(models.Model):
    item = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self):
        return f"item: {self.item} marca: {self.marca}" 
