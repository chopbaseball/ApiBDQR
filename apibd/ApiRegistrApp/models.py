from django.db import models

class Establecimiento(models.Model):
    id_establecimiento = models.IntegerField(primary_key=True)
    establecimiento = models.CharField(max_length=50)
    
    def str(self):
        return (self.establecimiento)

    class Meta:
        db_table = 'db_establecimiento'

class Alumno(models.Model):
    id_alumno = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    num_tel = models.CharField(max_length= 12)
    id_establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)

    def str(self):
        return (self.nombre)

    class Meta:
        db_table = 'db_alumno'

class Profesor(models.Model):
    id_profesor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    num_tel = models.CharField(max_length= 12)
    id_establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)

    def str(self):
        return (self.nombre)

    class Meta:
        db_table = 'db_profesor'

class Asignatura(models.Model):
    id_asignatura = models.IntegerField(primary_key=True)
    asignatura = models.CharField(max_length=50)

    def str(self):
        return (self.asignatura)

    class Meta:
        db_table = 'db_asignatura'

class Registro(models.Model):
    id_registro = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    id_establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)

    def str(self):
        return str(self.id_registro)

    class Meta:
        db_table = 'db_registro'

class Registro_Alumno(models.Model):
    id_registro = models.IntegerField()
    id_alumno = models.IntegerField()