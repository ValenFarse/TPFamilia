from django.shortcuts import render
from AppCoder.models import Mama, Papa, Hermano
from django.http import HttpResponse
from django.template import Context, Template, loader

# Create your views here.

def familia(self):

    pato= Mama(nombre="Patricia Galarza", dni= 26874316, fecha_de_nacimiento= 14-2-1986)

    pablo= Papa(nombre="Pablo Farsetti", dni= 24874316, fecha_de_nacimiento= 23-11-1982)
    fachi= Hermano(nombre="Fabrizio Farsetti", dni= 43874316, fecha_de_nacimiento= 25-8-2001)
    
    diccionario= {
        'Mama_nombre': pato.nombre,
        'Mama_dni': pato.dni,
        'Mama_fecha': pato.fecha_de_nacimiento,
        'Papa_nombre': pablo.nombre,
        'Papa_dni': pablo.dni,
        'Papa_fecha':pablo.fecha_de_nacimiento,
        'fachi_nombre': fachi.nombre,
        'fachi_dni': fachi.dni,
        'fachi_fecha': fachi.fecha_de_nacimiento,


    }


    plantilla=loader.get_template("template1.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)
