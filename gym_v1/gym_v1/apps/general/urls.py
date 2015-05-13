from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('gym_v1.apps.general.views',
	url(r'^add/producto/$','add_product_view',name='vista_agregar_producto'),
	)