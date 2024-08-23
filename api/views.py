import json
from django.http import JsonResponse

# Create your views here.
def index(request):
    data = {"message": "hello Quiz App"}
    return JsonResponse(data)
