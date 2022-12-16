from django.contrib import admin
from .models import *

class EstablecimientoAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_establecimiento','establecimiento']
        search_fields = ['id_establecimiento']

class AlumnoAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_alumno','nombre', 'apellido', 'rut', 'correo', 'password','num_tel', 'id_establecimiento'] 
        search_fields = ['id_alumno']

class ProfesorAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_profesor','nombre', 'apellido', 'rut', 'correo', 'password','num_tel', 'id_establecimiento']
        search_fields = ['id_profesor']

class AsignaturaAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_asignatura','asignatura'] 
        search_fields = ['id_asignatura']

class RegistroAdmin(admin.ModelAdmin):
    class Meta:
        list_display=['id_registro','fecha','id_profesor','id_asignatura','id_establecimiento'] 
        search_fields = ['id_registro']

class RegistroAlumnoAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['id_registro','id_alumno']
        search_fields = ['id_registro']

admin.site.register(Establecimiento,EstablecimientoAdmin)
admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Asignatura,AsignaturaAdmin)
admin.site.register(Registro,RegistroAdmin)
admin.site.register(Registro_Alumno,RegistroAlumnoAdmin)