from django.db import models


class cliente(models.Model):
	nombre 		= models.CharField(max_length=100)
	apellidos 	= models.CharField(max_length=100)
	status 		= models.BooleanField(default=True)
	# Membrsia, dia de la memblresia, etc

	def __unicode__(self):
		nombreCompleto = "%s %s" % (self.nombre, self.apellidos)
		return nombreCompleto

class producto(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Producto/%s/%s"%(self.nombre,str(filename))
		return ruta

	nombre		= models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200)
	status		= models.BooleanField(default=True)
	imagen		= models.ImageField(upload_to=url, null=True, blank=True)
	precio		= models.DecimalField(max_digits=6,decimal_places=2, null=True)
	stock		= models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return self.nombre