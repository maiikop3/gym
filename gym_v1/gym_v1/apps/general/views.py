from django.shortcuts import render_to_response
from django.template import RequestContext
from gym_v1.apps.general.forms import addProductForm
from gym_v1.apps.general.models import producto

def add_product_view(request):
	if request.method == "POST":
			form = addProductForm(request.POST,request.FILES)
			info = "inicianlizando"
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				descripcion = form.cleaned_data['descripcion']
				imagen = form.cleaned_data['imagen'] #se requiere request.FILES
				precio = form.cleaned_data['precio']
				stock = form.cleaned_data['stock']
				p = producto()
				p.nombre = nombre
				p.descripcion = descripcion
				if imagen: #validacion para imagen
					p.imagen = imagen
				p.precio = precio
				p.stock = stock
				p.status = True
				p.save() #guardar la informacion en P
				info = "Se guardo correctamente"
			else:
				info = "Informacion con datos incorrectos"
			form = addProductForm()
			ctx = {'form':form, 'informacion':info}
			return render_to_response('ventas/addproducto.html', ctx, context_instance=RequestContext(request))	

	else: 
		form = addProductForm()
		ctx = {'form':form} 	
		return render_to_response('ventas/addproducto.html',ctx, context_instance=RequestContext(request))