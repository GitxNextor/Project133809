# from django.shortcuts import render
from AppOne.models import Curso
from django.http import HttpResponse
# Create your views here.


def crea_curso(request):
    nombre_curso = "Desarrollo WEB"
    comision_curso = 741852
    print('Creando curso')
    curso = Curso(nombre=nombre_curso, comision=comision_curso)
    curso.save()
    respuesta = f"Curso creado: {curso.nombre} - {curso.comision}"
    return HttpResponse(respuesta)


def lista_cursos(request):
    cursos = Curso.objects.all()
    respuesta = ''
    for curso in cursos:
        respuesta += f'{curso.nombre} - {curso.comision}<br>'
    return HttpResponse(respuesta)
# Comentario pal git
