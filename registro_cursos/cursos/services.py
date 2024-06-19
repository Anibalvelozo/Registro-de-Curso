from .models import Curso, Profesor, Estudiante, Direccion

def crear_curso(nombre, descripcion):
    curso = Curso.objects.create(nombre=nombre, descripcion=descripcion)
    return curso

def crear_profesor(nombre, apellido, email):
    profesor = Profesor.objects.create(nombre=nombre, apellido=apellido, email=email)
    return profesor

def crear_estudiante(nombre, apellido, email, direccion):
    direccion_obj = Direccion.objects.create(**direccion)
    estudiante = Estudiante.objects.create(nombre=nombre, apellido=apellido, email=email, direccion=direccion_obj)
    return estudiante

def crear_direccion(calle, ciudad, pais):
    direccion = Direccion.objects.create(calle=calle, ciudad=ciudad, pais=pais)
    return direccion

def obtiene_estudiante(estudiante_id):
    return Estudiante.objects.get(id=estudiante_id)

def obtiene_profesor(profesor_id):
    return Profesor.objects.get(id=profesor_id)

def obtiene_curso(curso_id):
    return Curso.objects.get(id=curso_id)

def agrega_profesor_a_curso(profesor_id, curso_id):
    profesor = obtiene_profesor(profesor_id)
    curso = obtiene_curso(curso_id)
    curso.profesores.add(profesor)
    return curso

def agrega_cursos_a_estudiante(estudiante_id, cursos_ids):
    estudiante = obtiene_estudiante(estudiante_id)
    for curso_id in cursos_ids:
        curso = obtiene_curso(curso_id)
        curso.estudiantes.add(estudiante)
    return estudiante

def imprime_estudiante_cursos(estudiante_id):
    estudiante = obtiene_estudiante(estudiante_id)
    cursos = estudiante.curso_set.all()
    for curso in cursos:
        print(f"Curso: {curso.nombre}, Descripción: {curso.descripcion}")
