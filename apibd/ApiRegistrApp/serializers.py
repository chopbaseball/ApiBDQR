from .models import *
from rest_framework import serializers
from django.db.models import fields

class EstablecimientoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Establecimiento
        fields=['id_establecimiento','establecimiento'] 

class AlumnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields=['id_alumno','nombre', 'apellido', 'rut', 'correo', 'password','num_tel', 'id_establecimiento'] 

class ProfesorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields=['id_profesor','nombre', 'apellido', 'rut', 'correo','password', 'num_tel', 'id_establecimiento'] 

class AsignaturaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields=['id_asignatura','asignatura']

class RegistroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields=['id_registro','fecha','id_profesor','id_asignatura','id_establecimiento']

class Registro_AlumnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registro_Alumno
        fields= ['id_registro','id_alumno']