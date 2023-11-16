from django.db import models

class Alumno(models.Model):
    # Atributos y métodos de la clase Alumno
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

from django.db import models

class Genero(models.Model):
    idGenero = models.AutoField(primary_key=True, db_column='idGenero')
    tipoGenero = models.TextField(db_column='tipoGenero')

    class Meta:
        db_table = 'Generos'
