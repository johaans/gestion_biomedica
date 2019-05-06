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
        ('FACTURA',          {'fields': ['factura','factura_file']}),
        ('Fecha de compra',  {'fields':['factura_date'], 'classes': ['collapse']}),
        (None,               {'fields': ['pais']}),
        (None,               {'fields': ['importador']}),
        (None,               {'fields': ['riesgo']}),
        (None,               {'fields': ['uso']}),
        (None,               {'fields': ['ubicacion']}),
        ('INVIMA',           {'fields': ['invima','invima_file']}),
        ('IMPORTACION',      {'fields': ['importacion','importacion_file']}),
        ('MANUALES',         {'fields': ['manual_usuario', 'manual_instalacion', 'manual_mantenimiento','ubicacion_manuales','guia_rapida'], 'classes': ['collapse']}),
        ('MANTENIMIENTO',    {'fields': ['mantenimiento','calibracion','historico_mantenimiento','cronograma_general']}),
        ('IMAGEN',           {'fields': ['imagen']}),
        ('Fecha de publicacion',          {'fields':['created_date'],'classes': ['collapse']}),
    ]

    list_display = ('activo',)
    list_filter = ['activo','ubicacion','nombre']
    search_fields = ('activo','serie')

admin.site.register(task,ItemAdmin)
admin.site.register(project,projectAdmin)
admin.site.register(equipo,userAdmin)

