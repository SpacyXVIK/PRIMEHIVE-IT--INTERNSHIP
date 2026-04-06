from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Django backend is running",
        "success": True,
    })

def health(request):
    return JsonResponse({
        "status": "ok",
        "service": "backend",
    })