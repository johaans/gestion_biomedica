from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('404/', views.page_not_found,name='page_not_found'),
    path('', views.inicio, name='inicio'),
    path('list/', views.frequently_detail, name='frequently_detail'),
    path('noinvima/', views.noinvima, name='noinvima'),
    path('nomanual/', views.nomanual, name='nomanual'),
    path('noaplicainvima/', views.noaplicainvima, name='noaplicainvima'),
    path('nofactura/', views.nofactura, name='nofactura'),
    path('search/', views.search, name='search'),
    path('search/<int:pk>)/', views.equipo_detail, name='equipo_detail'),
    path('formulario/',views.formulario, name='formulario'),
    path('formulario/<int:pk>/edit/', views.formulario_edit, name='formulario_edit' )   ,
    path('counters/',views.counters, name='counters'),
    path('gestion/mantenimiento.pdf', views.pdf_view, name='pdf_view'),
    path('gestion/calibracion.pdf', views.pdf_view2, name='pdf_view2'),
    path('gestion/inventario.pdf', views.pdf_view3, name='pdf_view3'),
    path('tareas/',views.main,name='tareas'),
    path('set_done/<int:pk>/',views.set_done, name='set_done'),
    path('set_open/<int:pk>/',views.set_open,name='set_open'),
    path('drop/<int:pk>/',views.drop,name='drop'),
    path('create_project', views.create_project,name='create_project'),
    path('create_task',views.create_task,name='create_task'),
              ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'gestion.views.page_not_found'
#handler500 = 'gestion.views.handler500'
