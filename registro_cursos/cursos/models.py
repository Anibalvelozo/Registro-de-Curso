from django.db import models

class Direccion(models.Model):
    calle = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.calle}, {self.ciudad}, {self.pais}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    profesores = models.ManyToManyField(Profesor)
    estudiantes = models.ManyToManyField(Estudiante, through='Inscripcion')

    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)
