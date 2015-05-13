from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('gym_v1.apps.webServices.wsProductos.views',
	url(r'^ws/productos/$','wsProductos_view',name='ws_productos'),
	)