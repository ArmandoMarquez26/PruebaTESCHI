import pytest
from django.contrib.auth.models import User
from api.models import Ciudades, Consultas, Favoritos

@pytest.mark.django_db
def test_ciudades_model():
    # Crear una ciudad
    ciudad = Ciudades.objects.create(
        Ciudad='Ciudad de prueba',
    )

    # Obtener la ciudad desde la base de datos
    ciudad_db = Ciudades.objects.get(pk=ciudad.idCiudad)

    # Consultar datos de la ciudad
    assert ciudad_db.Ciudad == 'Ciudad de prueba'

    # Eliminar la ciudad
    ciudad_db.delete()


@pytest.mark.django_db
def test_consultas_model():
    # Crear un usuario de prueba
    usuario = User.objects.create(username='test_user')

    # Crear una ciudad
    ciudad = Ciudades.objects.create(
        Ciudad='Ciudad de prueba',
    )

    # Crear una consulta
    consulta = Consultas.objects.create(
        Temperatura=25.5,
        velViento='10 Km/h',
        Latitud='10 N',
        Longitud='20 W',
        Descripcion='Consulta de prueba',
        fk_Usuario=usuario,
        fk_Ciudad=ciudad,
    )

    # Obtener la consulta desde la base de datos
    consulta_db = Consultas.objects.get(pk=consulta.idConsulta)

    # Consultar datos de la consulta
    assert consulta_db.Temperatura == 25.5
    assert consulta_db.velViento == '10 Km/h'
    assert consulta_db.Latitud == '10 N'
    assert consulta_db.Longitud == '20 W'
    assert consulta_db.Descripcion == 'Consulta de prueba'
    assert consulta_db.fk_Usuario == usuario
    assert consulta_db.fk_Ciudad == ciudad

    # Eliminar la consulta y la ciudad asociada
    consulta_db.delete()
    ciudad.delete()


@pytest.mark.django_db
def test_favoritos_model():
    # Crear un usuario de prueba
    usuario = User.objects.create(username='test_user')

    # Crear una ciudad
    ciudad = Ciudades.objects.create(
        Ciudad='Ciudad de prueba',
    )

    # Crear un favorito
    favorito = Favoritos.objects.create(
        fk_Usuario=usuario,
        fk_Ciudad=ciudad,
    )

    # Obtener el favorito desde la base de datos
    favorito_db = Favoritos.objects.get(pk=favorito.idFavorito)

    # Consultar datos del favorito
    assert favorito_db.fk_Usuario == usuario
    assert favorito_db.fk_Ciudad == ciudad

    # Eliminar el favorito y la ciudad asociada
    favorito_db.delete()
    ciudad.delete()