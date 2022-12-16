from django.contrib import admin
from django.urls import re_path as path
from ApiRegistrApp import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
       
    path(r'^api/establecimiento/$',csrf_exempt(views.EstablecimientoViewSet.as_view())),
    path(r'^api/establecimiento/(?P<id_establecimiento>.+)/$',views.EstablecimientoSearchSet.as_view()),

    path(r'^api/alumno/$',csrf_exempt(views.AlumnoViewSet.as_view())),
    path(r'^api/alumno/(?P<id_alumno>.+)/$',views.AlumnoSearchSet.as_view()),

    path(r'^api/profesor/$',csrf_exempt(views.ProfesorViewSet.as_view())),
    path(r'^api/profesor/(?P<id_profesor>.+)/$',views.ProfesorSearchSet.as_view()),

    path(r'^api/asignatura/$',csrf_exempt(views.AsignaturaViewSet.as_view())),
    path(r'^api/asignatura/(?P<id_asignatura>.+)/$',views.AsignaturaSearchSet.as_view()),

    path(r'^api/registro/$',csrf_exempt(views.RegistroViewSet.as_view())),
    path(r'^api/registro/(?P<id_registro>.+)/$',views.RegistroSearchSet.as_view()),

    path(r'^api/registroAlumno/$',csrf_exempt(views.RegistroAlumnoViewSet.as_view())),
    path(r'^api/registroAlumno/(?P<id_registro>.+)/$',views.RegistroAlumnoSearchSet.as_view()),

]

