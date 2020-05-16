from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . models import Hamburguesa, Ingrediente
from . serializers import HamburguesaSerializer, IngredienteSerializer
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

PATH = 'https://tarea2-01.herokuapp.com/api/ingrediente/'
#PATH = "http://127.0.0.1:8000/api/ingrediente/"


@api_view(['GET', 'POST'])
def hamburguesa_list(request):
    """
        Listamos todas las hamburguesas
    """
    if request.method == 'GET':
        hamburguesa = Hamburguesa.objects.all()
        serializer = HamburguesaSerializer(hamburguesa, many=True)

        for burger in serializer.data:
            lista_url = []
            if burger["ingredientes"] != []:
                for ing in burger["ingredientes"]:
                    lista_url.append({ "path": f"{PATH}{ing}"})
                burger["ingredientes"] = lista_url
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = HamburguesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def hamburguesa_detail(request, pk):
    """
        Para get, put o delete de las burgers :)
    """
    try:
        hamburguesa = Hamburguesa.objects.get(pk=pk)
    except Hamburguesa.DoesNotExist:
        return Response({'message': 'Hamburguesa inexistente'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HamburguesaSerializer(hamburguesa)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        no_permitidos = ["id", "ingredientes"]
        if any(x in request.data.keys() for x in no_permitidos):
            return JsonResponse({'message': 'Parámetros inválidos'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = HamburguesaSerializer(hamburguesa, data=request.data, partial=True)
        if serializer.is_valid():
            hamburguesa_entry = serializer.save()
            return JsonResponse({'message': 'Operación Exitosa'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': 'Parámetros inválidos'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hamburguesa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'DELETE'])
def ingrediente_en_hamurguesa_detail(request, id1, id2):
    """
        Para get, put o delete de los ingredientes de las burgers :)
    """
    try:
        hamburguesa = Hamburguesa.objects.get(pk=id1)
        # print("los ing son")
        # print(hamburguesa.id_ingredientes)
    except Hamburguesa.DoesNotExist:
        return Response({'message': 'Id de hamburguesa inválido'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        ingrediente = Ingrediente.objects.get(pk=id2)
    except Ingrediente.DoesNotExist:
        return Response({'message': 'Ingrediente inexistente'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        # Si paso, es porque la hamburguesa existe, entonces verificamos que el ingrediente también
        serializer = HamburguesaSerializer(hamburguesa)
        if id2 in serializer.data["ingredientes"]:
             return JsonResponse({'message': 'Ingrediente agregado'}, status=status.HTTP_201_CREATED)
        hamburguesa.ingredientes.add(ingrediente)
        return JsonResponse({'message': 'Ingrediente agregado'}, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        serializer = HamburguesaSerializer(hamburguesa)
        if id2 not in serializer.data["ingredientes"]:
            return JsonResponse({'message': 'Ingrediente inexistente en la hamburguesa'},status=status.HTTP_404_NOT_FOUND)
        hamburguesa.ingredientes.remove(ingrediente)
        print(serializer.data["ingredientes"])
        return JsonResponse({'message': 'Ingrediente retirado'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def ingrediente_list(request):
    """
        Listamos todas las hamburguesas
    """
    if request.method == 'GET':
        ingrediente = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingrediente, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = IngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def ingrediente_detail(request, pk):
    """
        Para get, put o delete de las burgers :)
    """
    try:
        ingrediente = Ingrediente.objects.get(pk=pk)
    except Ingrediente.DoesNotExist:
        return Response({'message': 'Ingrediente inexistente'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        hamburguesa = Hamburguesa.objects.all()
        serializer = HamburguesaSerializer(hamburguesa, many=True)
        ing_all = []
        for burger in serializer.data:
            ing_all += burger["ingredientes"]
        if pk in ing_all:
            return Response({'message': 'Ingrediente no se puede borrar, se encuentra presente en una hamburguesa'}, status=status.HTTP_200_OK)
        ingrediente.delete()
        return Response({'message': 'Ingrediente eliminado'}, status=status.HTTP_200_OK)



