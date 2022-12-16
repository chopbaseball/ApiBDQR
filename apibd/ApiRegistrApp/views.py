from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

class EstablecimientoViewSet(generics.ListCreateAPIView):
    queryset = Establecimiento.objects.all()
    serializer_class = EstablecimientoSerializers

class EstablecimientoSearchSet(generics.ListCreateAPIView):
    serializer_class = EstablecimientoSerializers
    def get_queryset(self):
        id = self.kwargs['id_establecimiento']
        return Establecimiento.objects.filter(id_establecimiento=id)

class AlumnoViewSet(generics.ListCreateAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializers

class AlumnoSearchSet(generics.ListCreateAPIView):
    serializer_class = AlumnoSerializers
    def get_queryset(self):
        id = self.kwargs['id_alumno']
        return Alumno.objects.filter(id_alumno=id)

class ProfesorViewSet(generics.ListCreateAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializers

class ProfesorSearchSet(generics.ListCreateAPIView):
    serializer_class = ProfesorSerializers
    def get_queryset(self):
        id = self.kwargs['id_profesor']
        return Profesor.objects.filter(id_profesor=id)

class AsignaturaViewSet(generics.ListCreateAPIView):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializers

class AsignaturaSearchSet(generics.ListCreateAPIView):
    serializer_class = AsignaturaSerializers
    def get_queryset(self):
        id = self.kwargs['id_asignatura']
        return Asignatura.objects.filter(id_asignatura=id)

class RegistroViewSet(generics.ListCreateAPIView):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializers

class RegistroSearchSet(generics.ListCreateAPIView):
    serializer_class = RegistroSerializers
    def get_queryset(self):
        id = self.kwargs['id_registro']
        return Registro.objects.filter(id_registro=id)

class RegistroAlumnoViewSet(generics.ListCreateAPIView):
    queryset = Registro_Alumno.objects.all()
    serializer_class = Registro_AlumnoSerializers

class RegistroAlumnoSearchSet(generics.ListCreateAPIView):
    serializer_class = Registro_AlumnoSerializers
    def get_queryset(self):
        id = self.kwargs['id_registro']
        return Registro_Alumno.objects.filter(id_registro=id)