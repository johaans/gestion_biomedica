from django.db import models

# Create your models here.
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

class project(models.Model):
    name = models.CharField(max_length = 60,unique=True)


class task(models.Model):
    name = models.CharField(max_length = 60)
    user = models.ForeignKey(User, blank=True, null=True , on_delete=models.CASCADE)
    creation_date =  models.DateTimeField(auto_now_add = True)
    finalization_date = models.DateTimeField(null = True, blank = True)
    priority = models.PositiveSmallIntegerField(default = 0)
    difficulty = models.PositiveSmallIntegerField(default = 0)
    project = models.ForeignKey(project, null = True, blank = True,on_delete=models.CASCADE)

    def set_done(self):
        self.finalization_date = timezone.now()
    def set_open(self):
        self.finalization_date = None
    def priority_str(self):
        if self.priority == 0:
            return "Baja"
        if self.priority == 1:
            return "Normal"
        if self.priority == 2:
            return "Alta"
        return "Sin definir"
    def difficulty_str(self):
        if self.difficulty == 0:
            return u"Muy fácil"
        if self.difficulty == 1:
            return u"Fácil"
        if self.difficulty == 2:
            return u"Normal"
        if self.difficulty == 3:
            return u"Difícil"
        if self.difficulty == 4:
            return u"Muy difícil"
        return "Sin definir"
    def project_str(self):
        if self.project == None:
            return "Sin definir"
        return self.project.name
    def user_str(self):
        if self.user == None:
            return "Todo el mundo"
        return self.user.username

class equipo(models.Model):
    im="uploads/imagenes/no_im.jpg"
    si="si"
    no="no"
    na="N/A"
    opciones=((si,"si"),(no,"no"),(na,"N/A"))
    q1="quirofano 1"
    q2="quirofano 2"
    q3="quirofano 3"
    q4="quirofano 4"
    central="central de esterilizacion"
    recuperacion="recuperacion"
    preparacion="preparacion"
    procedimientos_menores="procedimientos menores"
    consultorio_1="consultorio anestesia"
    consultorio_2="consultorio 2"
    otro="otro"
    servicios=(
        (q1,"quirofano 1"),
        (q2,"quirofano 2"),
        (q3,"quirofano 3"),
        (q4,"quirofano 4"),
        (central,"central de esterilizacion"),
        (recuperacion,"recuperacion"),
        (preparacion,"preparacion"),
        (procedimientos_menores,"procedimientos menores"),
        (consultorio_1,"consultorio anestesia"),
        (consultorio_2,"consultorio 2"),
        (otro,"otro"),
    )
    uno="1"
    dosa="2A"
    dosb="2B"
    tres="3"
    riesgo_op=(
        (uno,"I"),
        (dosa,"IIA"),
        (dosb,"IIB"),
        (tres,"III"),
        (na,"N/A"))
    estetica="estetica"
    diagnostico="diagnostico"
    laboratorio="laboratorio"
    prevencion="prevencion"
    rehabilitacion="rehabilitacion"
    soporte_vital="soporte vital"
    tratamiento="tratamiento"
    uso_op=(
        (estetica,"estetica"),
        (diagnostico,"diagnostico"),
        (laboratorio,"laboratorio"),
        (prevencion,"prevencion"),
        (rehabilitacion,"rehabilitacion"),
        (soporte_vital,"soporte vital"),
        (tratamiento,"tratamiento"),
        (na,"N/A"),
    )
    nombre = models.CharField('NOMBRE',max_length=25)
    marca = models.CharField('MARCA',max_length=40,null=True,blank=True)
    modelo = models.CharField('MODELO',max_length=25)
    serie= models.CharField('SERIE', max_length=100,unique=True)
    activo = models.CharField('ACTIVO',max_length=25, null=True,blank=True,unique=True,help_text=" <strong>Para Equipos Alquilados Ingrese El Rango <em>De 210 En Adelante</em>.</strong>")
    archivo_hoja_de_vida=models.FileField(upload_to='uploads/hv/%Y/%m/',null=True,blank=True)
    factura=models.CharField(max_length=3,choices=opciones,default=no)
    fecha_factura = models.DateField(blank=True, null=True,help_text="<strong>Por favor usar el siguiente formsto: <em>DD-MM-YYYY</em>.</strong>")
    archivo_factura=models.FileField(upload_to='uploads/fact/%Y/%m/',null=True,blank=True)
    importador=models.CharField(max_length=30,blank=True,null=True)
    riesgo=models.CharField(max_length=3,choices=riesgo_op,default=na)
    uso=models.CharField(max_length=100,choices=uso_op,default=na)
    ubicacion= models.CharField('UBICACION',max_length=25,choices=servicios,default=otro)
    invima=models.CharField(max_length=3,choices=opciones,default=na)
    arhivo_invima=models.FileField(upload_to='uploads/inv/%Y/%m/',null=True,blank=True)
    importacion=models.CharField(max_length=3,choices=opciones,default=no)
    archivo_importacion=models.FileField(upload_to='uploads/impor/%Y/%m/',null=True,blank=True)
    manual_usuario=models.CharField(max_length=3,choices=opciones,default=no)
    manual_funcionamiento=models.CharField(max_length=3,choices=opciones,default=no)
    manual_instalacion=models.CharField(max_length=3,choices=opciones,default=no)
    manual_mantenimiento=models.CharField(max_length=3,choices=opciones,default=no)
    ubicacion_manuales=models.CharField(max_length=20,null=True,blank=True)
    guia_rapida=models.CharField(max_length=3,choices=opciones,default=no)
    mantenimiento=models.CharField(max_length=3,choices=opciones,default=no)
    calibracion=models.CharField(max_length=3,choices=opciones,default=na)
    historico_mantenimiento=models.FileField(upload_to='uploads/cronom/%Y/%m/',null=True,blank=True)
    cronograma_general=models.FileField(upload_to='uploads/cronocal/%Y/%m/',null=True,blank=True)
    imagen=models.ImageField(upload_to='uploads/imagenes',null=True,blank=True, default=im)
    created_date = models.DateTimeField(default=timezone.now)
    observacion=models.TextField(max_length=999,null=True,blank=True)




    def __str__(self):
        return self.activo


