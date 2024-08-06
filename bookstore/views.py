# C:\Users\profe\Desktop\BOOKSTORE\bookstore\views.py

from django.http import JsonResponse
from django.shortcuts import render

def update(request):
    # Lógica para a view de atualização
    return JsonResponse({"status": "update successful"})

def hello_world(request):
    # Lógica para a view de hello world
    return JsonResponse({"message": "Hello, world!"})
