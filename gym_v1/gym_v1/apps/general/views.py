from django.shortcuts import render_to_response
from django.template import RequestContext
from gym_v1.apps.general.forms import addProductForm
from gym_v1.apps.general.models import producto
from django.http import HttpResponseRedirect

def add_product_view(request):
	info = "inicianlizando"
	if request.method == "POST":
		form = addProductForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.status
			add.save() #save info
			form.save_m2m()#guarda las relacion de ManyToMany
			info = "Guardado Satisfactoriamente!"
			return HttpResponseRedirect('/producto/%s'%add.id)
	else:
		form = addProductForm()
	ctx = {'form':form, 'informacion':info}
	return render_to_response('ventas/addproducto.html', ctx, context_instance=RequestContext(request))	


def edit_product_view(request,id_prod):
	info = "inicianlizando"
	prod = producto.objects.get(pk=id_prod)
	if request.method == "POST":
		form = addProductForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit_prod = form.save(commit=False)
			form.save_m2m()
			edit_prod.status = True
			edit_prod.save() #se guarda el objecto
			info = "Correcto"
			return HttpResponseRedirect('/producto/%s'%edit_prod.id)

		
	else:
		form = addProductForm(instance=prod)
	ctx = {'form':form, 'informacion':info, 'prod':prod}
	return render_to_response('ventas/editProducto.html', ctx, context_instance=RequestContext(request))



"""
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
				info = "Se guardo correctamente!"
			else:
				info = "Informacion con datos incorrectos"
			form = addProductForm()
			ctx = {'form':form, 'informacion':info}
			return render_to_response('ventas/addproducto.html', ctx, context_instance=RequestContext(request))	

	else: 
		form = addProductForm()
		ctx = {'form':form} 	
		return render_to_response('ventas/addproducto.html',ctx, context_instance=RequestContext(request))




def edit_product_view(request,id_prod):
	p = producto.objects.get(id=id_prod)
	if request.method == "POST":
		form = addProductForm(request.POST, request.FILES)
		if form.is_valid():
			nombre 		= form.cleaned_data['nombre']
			descripcion = form.cleaned_data['descripcion']
			precio 		= form.cleaned_data['precio']
			imagen 		= form.cleaned_data['imagen']
			stock 		= form.cleaned_data['stock']
			p.nombre 		= nombre
			p.descripcion 	= descripcion
			p.precio	 	= precio
			if imagen: #verificacion para que la imagen sea correcta
				p.imagen = imagen
			p.save() #guardar en EDITAR
			return HttpResponseRedirect('/producto/%s'%p.id)

	if request.method == "GET":
		form = addProductForm(initial={
			'nombre':p.nombre,
			'descripcion':p.descripcion,
			'precio':p.precio,
			'stock':p.stock,
			#'imagen':p.imagen,
			})
	ctx = {'form':form, 'producto':p}	
	return render_to_response('ventas/editProducto.html', ctx, context_instance=RequestContext(request))


"""