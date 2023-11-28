from django.http import JsonResponse
from .models import MyModel
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
@require_http_methods(["GET", "POST"])
def my_model_view(request):
    """
    View to handle GET and POST requests for the MyModel.
    
    GET: Returns a list of all MyModel items.
    POST: Creates a new MyModel item with the provided data.
    """
    if request.method == 'GET':
        # Handle GET request
        items = list(MyModel.objects.values())
        return JsonResponse(items, safe=False)
    elif request.method == 'POST':
        # Handle POST request
        data = json.loads(request.body)
        item = MyModel.objects.create(**data)
        return JsonResponse({'id': item.id}, status=201)
    
@csrf_exempt
@require_http_methods(["PUT", "DELETE"])
def my_model_detail_view(request, id):
    """
    View to handle PUT and DELETE requests for a MyModel item by id.
    
    PUT: Updates the specified MyModel item with the provided data.
    DELETE: Deletes the specified MyModel item.
    """
    if request.method == 'PUT':
        # Handle PUT request
        data = json.loads(request.body)
        try:
            item = MyModel.objects.get(id=id)
            for field, value in data.items():
                setattr(item, field, value)
            item.save()
            return JsonResponse({'id': item.id}, status=200)
        except MyModel.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=404)
    elif request.method == 'DELETE':
        # Handle DELETE request
        try:
            item = MyModel.objects.get(id=id)
            item.delete()
            return JsonResponse({'message': 'Item deleted'}, status=200)
        except MyModel.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=404)
