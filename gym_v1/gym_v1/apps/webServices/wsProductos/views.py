# Create your views here.
from django.http import HttpResponse
from gym_v1.apps.general.models import producto
#serializacion de los objetos
from django.core import serializers

def wsProductos_view(request):
	data = serializers.serialize("json",producto.objects.filter(status=True))
	#Regresa info en formato json
	return HttpResponse(data,content_type='application/json')