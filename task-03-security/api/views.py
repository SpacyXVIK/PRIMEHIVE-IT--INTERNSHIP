from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .services import build_health_response, build_signup_payload
from .validators import validate_username, validate_password

def health_check(request):
    if request.method != "GET":
        return JsonResponse(
            {"status": "error", "message": "Method not allowed"},
            status=405
        )

    return JsonResponse(build_health_response(), status=200)

def signup_preview(request):
    if request.method != "GET":
        return JsonResponse(
            {"status": "error", "message": "Method not allowed"},
            status=405
        )

    username = request.GET.get("username")
    password = request.GET.get("password")

    username_error = validate_username(username)
    if username_error:
        return JsonResponse(
            {"status": "error", "message": username_error},
            status=400
        )

    password_error = validate_password(password)
    if password_error:
        return JsonResponse(
            {"status": "error", "message": password_error},
            status=400
        )

    payload = build_signup_payload(username, password)

    return JsonResponse(
        {
            "status": "success",
            "message": "Input validated successfully",
            "data": {
                "username": payload["username"],
                "password_hash": payload["password_hash"]
            }
        },
        status=200
    )