import json
from django.http import JsonResponse

# Create your views here.
def api_home(request, *args, **kwargs):
    body = request.body
    data = {"message":"Hi there!"}
    print(request.GET)
    print(request.POST)
    try:
        data = json.loads(body)
    except:
        pass
    return JsonResponse(data)
