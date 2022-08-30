from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    asunto=models.TextField()
    
    def __str__(self):
        return self.nombre
    
class Gatos(models.Model):
    class Meta:
        db_table = 'tabla_gatos'
        
    gato_name=models.CharField(max_length=50)
    raza=models.CharField(max_length=50)
    fecha=models.CharField(max_length=150)
    
    def __str__(self):
        return self.nombre
    
class Postulacion(models.Model):
    class Meta:
        db_table = 'tabla_postulaciones'
    
    
    email = models.EmailField(max_length=150)
    rut = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    fecha_nac = models.DateTimeField()
    telefono = models.CharField(max_length=15)
    regiones = models.CharField(max_length=250)
    comunas = models.CharField(max_length=150)
    direccion=models.CharField(max_length=250,default='SOME STRING' )
    tipo_vivienda = models.CharField(max_length=50)
    gato=models.ForeignKey(Gatos,on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s %s" % (self.username)