from django.db import models
from django.contrib.auth.models import User

class Alumno(models.Model):
    # Atributos y métodos de la clase Alumno
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    idGenero = models.AutoField(primary_key=True, db_column='idGenero')
    tipoGenero = models.TextField(db_column='tipoGenero')

    class Meta:
        db_table = 'Generos'

class Ciudades(models.Model):
    idCiudad = models.AutoField(primary_key=True,default=1,db_column="idCiudad")
    Ciudad = models.CharField(max_length=50,default="Ciudad",db_column="Ciudad")
    class Meta:
        db_table="Ciudades"

class Consultas(models.Model):
    idConsulta = models.AutoField(primary_key=True,default=1,db_column="idConsulta")
    Temperatura = models.FloatField(default=0.1,db_column="Temperatura")
    velViento = models.CharField(max_length=10,default="0 Km/h",db_column="velViento")
    Latitud = models.CharField(max_length=10,default="0 N",db_column="Latitud")
    Longitud = models.CharField(max_length=10,default="0 W",db_column="Longitud")
    Descripcion = models.CharField(max_length=45,default="Descripcion",db_column="Descripcion")
    fk_Usuario = models.ForeignKey(User,on_delete=models.CASCADE,db_column='fk_Usuario')
    fk_Ciudad = models.ForeignKey(Ciudades,on_delete=models.CASCADE,db_column='fk_Ciudad')
    class Meta:
        db_table="Consultas"
        
class Favoritos(models.Model):
    idFavorito = models.AutoField(primary_key=True,db_column="idFavorito")
    fk_Usuario = models.ForeignKey(User,on_delete=models.CASCADE,db_column='fk_Usuario')
    fk_Ciudad = models.ForeignKey(Ciudades,on_delete=models.CASCADE,db_column='fk_Ciudad')