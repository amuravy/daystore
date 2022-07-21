from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from agencia.models import Auto, Marca

# Create your views here.


class AutoView(APIView):

    permission_classes = []

    def post(self, request):
        nombre = request.data.get('nombre')
        marca = request.data.get('marca')
        color = request.data.get('color')

        if nombre == '':
            return Response('El nombre es requerido', status=status.HTTP_400_BAD_REQUEST)

        if marca == '':
            return Response('La marca es requerido',
                            status=status.HTTP_400_BAD_REQUEST)

        if color == '':
            return Response('El color es requerido',
                            status=status.HTTP_400_BAD_REQUEST)

        marca_guardada, _ = Marca.objects.get_or_create(nombre=marca)
        auto = Auto.objects.create(nombre=nombre, marca=marca_guardada, color=color)

        return Response('Auto creado', status.HTTP_201_CREATED)





