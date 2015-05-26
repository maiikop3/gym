# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from gym_v1.apps.general.models import producto
from gym_v1.apps.home.forms import ContactForm, LoginForm
from django.core.mail import EmailMultiAlternatives #envio html
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect

def index_view(request):
	return render_to_response('home/index.html', context_instance=RequestContext(request))

def about_view(request):
	mensaje = "Mensaje desde views.py"
	ctx = {'msg':mensaje}
	return render_to_response('home/about.html',ctx, context_instance=RequestContext(request))

def productos_view(request, pagina):
	lista_prod = producto.objects.filter(status=True)
	paginator = Paginator(lista_prod,5)#productos por pagina
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)
	except(EmptyPage, InvalidPage):
		productos = paginator.page(paginator.num_pages)
	ctx = {'productos':productos}
	return render_to_response('home/productos.html' ,ctx, context_instance=RequestContext(request))



def soloProducto_view(request, id_prod):
	prod = producto.objects.get(id=id_prod)
	cats = prod.categorias.all() #categorias del producto
	ctx = {'producto':prod, 'categorias':cats}
	return render_to_response('home/soloproducto.html', ctx, context_instance=RequestContext(request))

#formulario para envio de emails
def contacto_view(request):
	info_enviado = False
	email =""
	titulo=""
	texto=""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']

			#configuracion envio email
			to_admin = 'm.machuca.osuna@gmail.com'
			html_content = "Informacion recibida de: [%s]<br><br><br>***MENSAJE***<br><br>%s"%(email,texto)
			msg = EmailMultiAlternatives('Correo de contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')#se define el contenido como html
			msg.send()

	else:		
		formulario = ContactForm()
	ctx = {'form':formulario, 'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
	return render_to_response('home/contacto.html', ctx, context_instance=RequestContext(request))


def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return	HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
					#return HttpResponseRedirect('/inicio/') AL ADMIN
				else:
					mensaje = "Usuario y/o Password incorrectas. Intenta de nuevo."
		form = LoginForm()
		ctx = {'form':form, 'mensaje':mensaje}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')



#--- Pruebas Admin ---

def index_admin_view(request):
	return render_to_response('home/indexAdmin.html', context_instance=RequestContext(request))

def productos_admin_view(request):
	return render_to_response('home/adminProductos.html', context_instance=RequestContext(request))
