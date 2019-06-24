# Register your models here.
from .models import equipo
from django.contrib import admin
from .models import task, project

class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "priority", "difficulty", "creation_date"]
    search_fields = ["name"]
class projectAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


class userAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nombre']}),
        (None,               {'fields': ['modelo']}),
        (None,               {'fields': ['serie']}),
        (None,               {'fields': ['activo']}),
        (None,               {'fields': ['hv_file']}),
        ('FACTURA',          {'fields': ['factura','archivo_factura']}),
        ('Fecha de compra',  {'fields':['fecha_factura'], 'classes': ['collapse']}),
        (None,               {'fields': ['importador']}),
        (None,               {'fields': ['riesgo']}),
        (None,               {'fields': ['uso']}),
        (None,               {'fields': ['ubicacion']}),
        ('INVIMA',           {'fields': ['invima','archivo_invima']}),
        ('IMPORTACION',      {'fields': ['importacion','archivo_importacion']}),
        ('MANUALES',         {'fields': ['manual_usuario', 'manual_instalacion', 'manual_mantenimiento','ubicacion_manuales','guia_rapida'], 'classes': ['collapse']}),
        ('MANTENIMIENTO',    {'fields': ['mantenimiento','calibracion','historico_mantenimiento','cronograma_general']}),
        ('IMAGEN',           {'fields': ['imagen']}),
        ('Fecha de publicacion',          {'fields':['created_date'],'classes': ['collapse']}),
        ('Observaciones',    {'fields': ['observacion']}),
    ]

    list_display = ('activo',)
    list_filter = ['activo','ubicacion','nombre']
    search_fields = ('activo','serie')

admin.site.register(task,ItemAdmin)
admin.site.register(project,projectAdmin)
admin.site.register(equipo,userAdmin)

