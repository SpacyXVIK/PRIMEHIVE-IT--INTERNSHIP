from django.shortcuts import render

from django.http import JsonResponse

def health_check(request):
    if request.method == 'GET':
        return JsonResponse(
            {
                'status': 'success',
                'message': 'Bcakend is running successfully'
            },
            status=200
            )
    return JsonResponse(
        {
            'status': 'error',
            'message': 'Method not allowed'
        },
        status=405
    )

# Create your views here.
