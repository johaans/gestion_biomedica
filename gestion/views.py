from django.shortcuts import render, render_to_response, get_object_or_404, redirect,HttpResponse
from django.views.generic.base import View
from django.template import RequestContext
#from django.views.decorators import csrf
from django.contrib.admin.views.decorators import staff_member_required
from .models import task, project
from .models import equipo
from django.db.models import Q
from .models import equipo
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import equipoModelForm
from django.core.paginator import Paginator
# Create your views here.

@login_required
def inicio(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_equipos=equipo.objects.all().count()
    nprojects = project.objects.count()
    ntasks_todo = task.objects.filter(Q(user = request.user) | Q(user = None)).filter(finalization_date = None).count()
    ntasks_done = task.objects.filter(Q(user = request.user) | Q(user = None)).exclude(finalization_date = None).count()
    # Filtro de datos
    tasks_todo = task.objects.filter(Q(user = request.user) | Q(user = None)).filter(finalization_date = None).order_by( "creation_date" , "difficulty")
    tasks_done = task.objects.filter(Q(user = request.user) | Q(user = None)).exclude(finalization_date = None).order_by("-finalization_date")
    projects = project.objects.all().order_by("name")
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    return render(request, 'gestion/inicio.html',
                  context={'num_equipos':num_equipos,
                           'num_visits':num_visits,
                           'tasks_done':tasks_done,
                           'tasks_todo':tasks_todo,'ntasks_todo':ntasks_todo,
                           'ntasks_done':ntasks_done,'user':request.user,
                           'projects':projects,'nprojects':nprojects,}
                  )
@login_required
def counters(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_equipos=equipo.objects.all().count()
    num_na_invima=equipo.objects.filter(invima__exact='N/A').count()
    num_no_invima=equipo.objects.filter(invima__exact='no').count()
    num_no_factura=equipo.objects.filter(factura__exact='no').count()
    num_na_importacion=equipo.objects.filter(importacion__exact='N/A').count()
    num_no_importacion=equipo.objects.filter(importacion__exact='no').count()
    num_no_mantenimiento=equipo.objects.filter(mantenimiento__exact='no').count()
    num_na_calibracion=equipo.objects.filter(calibracion__exact='N/A').count()
    num_no_calibracion=equipo.objects.filter(calibracion__exact='no').count()
    num_no_musuario=equipo.objects.filter(manual_usuario__exact='no').count()
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    return render(request, 'gestion/counters.html',
                  context={'num_equipos':num_equipos,'num_visits':num_visits,
                           'num_na_invima':num_na_invima,'num_no_invima':num_no_invima,
                           'num_no_factura':num_no_factura,'num_na_importacion':num_na_importacion,
                           'num_no_importacion':num_no_importacion,'num_no_mantenimiento':num_no_mantenimiento,
                           'num_na_calibracion':num_na_calibracion,'num_no_calibracion':num_no_calibracion,
                           'num_no_musuario' : num_no_musuario,
                           },
)

@login_required
def frequently_detail(request):
    posts = equipo.objects.all().order_by('activo')
    paginator = Paginator(posts, 3 ) # Show 3 contacts per page
    page = request.GET.get('page')
    try:
        profiles = paginator.page(page)
    except :
        profiles = paginator.page(1)

    equipos=paginator.get_page(page)

    return render(request, 'gestion/frequently_detail.html', {'equipos': equipos})

@login_required
def noaplicainvima(request):
    nainvima = equipo.objects.filter(invima__exact='N/A').order_by('activo')
    paginator = Paginator(nainvima, 3 ) # Show 3 contacts per page
    page = request.GET.get('page')
    try:
        profiles = paginator.page(page)
    except :
        profiles = paginator.page(1)

    equipos=paginator.get_page(page)
    return render(request, 'gestion/noaplicainvima.html', {'equipos': equipos})

@login_required
def noinvima(request):
    sininvima = equipo.objects.filter(invima__exact='no').order_by('activo')
    paginator = Paginator(sininvima, 3 ) # Show 3 contacts per page
    page = request.GET.get('page')
    try:
        profiles = paginator.page(page)
    except :
        profiles = paginator.page(1)

    equipos=paginator.get_page(page)
    return render(request, 'gestion/noinvima.html', {'equipos': equipos})
@login_required
def nomanual(request):
    sinmanual = equipo.objects.filter(manual_usuario__exact='no').order_by('activo')
    paginator = Paginator(sinmanual, 3 ) # Show 3 contacts per page
    page = request.GET.get('page')
    try:
        profiles = paginator.page(page)
    except :
        profiles = paginator.page(1)

    equipos=paginator.get_page(page)
    return render(request, 'gestion/nomanual.html', {'equipos': equipos})

@login_required
def nofactura(request):
    sinfactura = equipo.objects.filter(factura__exact='no').order_by('activo')
    paginator = Paginator(sinfactura, 3 ) # Show 3 contacts per page
    page = request.GET.get('page')
    try:
        profiles = paginator.page(page)
    except :
        profiles = paginator.page(1)

    equipos=paginator.get_page(page)
    return render(request, 'gestion/nofactura.html', {'equipos': equipos})

@login_required
def noaplicacalibracion(request):
    nacalibracion = equipo.objects.filter(calibracion__exact='N/A').order_by('activo')
    paginator = Paginator(nacalibracion, 3 ) # Show 3 contacts per page
    page = request.GET.get('page')
    try:
        profiles = paginator.page(page)
    except :
        profiles = paginator.page(1)

    equipos=paginator.get_page(page)
    return render(request, 'gestion/noaplicacalibracion.html', {'equipos': equipos})
@login_required
def noaplicaimportacion(request):
    naimpor = equipo.objects.filter(importacion__exact='N/A').order_by('activo')
    paginator = Paginator(naimpor, 3 ) # Show 3 contacts per page
    page = request.GET.get('page')
    try:
        profiles = paginator.page(page)
    except :
        profiles = paginator.page(1)

    equipos=paginator.get_page(page)
    return render(request, 'gestion/noaplicaimportacion.html', {'equipos': equipos})
@login_required
def nocalibracion(request):
    nocal = equipo.objects.filter(calibracion__exact='no').order_by('activo')
    paginator = Paginator(nocal, 3 ) # Show 3 contacts per page
    page = request.GET.get('page')
    try:
        profiles = paginator.page(page)
    except :
        profiles = paginator.page(1)

    equipos=paginator.get_page(page)
    return render(request, 'gestion/nocalibracion.html', {'equipos': equipos})
@login_required
def noimportacion(request):
    noimpor = equipo.objects.filter(importacion__exact='no').order_by('activo')
    paginator = Paginator(noimpor, 3 ) # Show 3 contacts per page
    page = request.GET.get('page')
    try:
        profiles = paginator.page(page)
    except :
        profiles = paginator.page(1)

    equipos=paginator.get_page(page)
    return render(request, 'gestion/noimportacion.html', {'equipos': equipos})
@login_required
def nomantenimiento(request):
    noman = equipo.objects.filter(mantenimiento__exact='no').order_by('activo')
    paginator = Paginator(noman, 3 ) # Show 3 contacts per page
    page = request.GET.get('page')
    try:
        profiles = paginator.page(page)
    except :
        profiles = paginator.page(1)

    equipos=paginator.get_page(page)
    return render(request, 'gestion/nomantenimiento.html', {'equipos': equipos})
@login_required
def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(activo__icontains=query) | Q(nombre__icontains=query) | Q(serie__icontains=query)
            | Q(ubicacion__icontains=query) | Q(importador__icontains=query)
        )
        results = equipo.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("gestion/search.html", {
        "results": results,
        "query": query
    })
@staff_member_required
def equipo_detail(request,pk):
    post = get_object_or_404(equipo, pk=pk)
    return render(request, 'gestion/equipo_detail.html', {'post': post})
@login_required
def formulario(request):
    if request.method == "POST":
        form = equipoModelForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.created_date = timezone.now()
                post.save()
                return redirect('equipo_detail', pk=post.pk)
            except:
                print("Error")
    else:
        form = equipoModelForm()
    return render(request, 'gestion/formulario.html', {'form': form})
@login_required
def formulario_edit(request, pk):
    post = get_object_or_404(equipo, pk=pk)
    if request.method == "POST":
        form = equipoModelForm(request.POST or None,request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('equipo_detail', pk=post.pk)
    else:
        form = equipoModelForm(instance=post)
    return render(request, 'gestion/formulario.html', {'form': form})





@login_required
def main(request):
    # Numero de objetos
    nprojects = project.objects.count()
    ntasks_todo = task.objects.filter(Q(user = request.user) | Q(user = None)).filter(finalization_date = None).count()
    ntasks_done = task.objects.filter(Q(user = request.user) | Q(user = None)).exclude(finalization_date = None).count()
    # Filtro de datos
    tasks_todo = task.objects.filter(Q(user = request.user) | Q(user = None)).filter(finalization_date = None).order_by( "creation_date" , "difficulty")
    tasks_done = task.objects.filter(Q(user = request.user) | Q(user = None)).exclude(finalization_date = None).order_by("-finalization_date")
    projects = project.objects.all().order_by("name")
    return render(request, 'index.html',context={'tasks_done':tasks_done,
                                                 'tasks_todo':tasks_todo,'ntasks_todo':ntasks_todo,
                                                 'ntasks_done':ntasks_done,'user':request.user,
                                                 'projects':projects,'nprojects':nprojects,}
    )
@login_required()
def create_task(request):
    if request.method == 'POST':
        l_name = request.POST.get('name')
        l_priority = request.POST.get('priority')
        l_difficulty = request.POST.get('difficulty')
        l_project = request.POST.get('project')
        l_user = request.POST.get('user')

        if l_project != None:
            lo_project = project.objects.get(pk = l_project)
            if l_user != None:
                lo_user = request.user
                l_task = task.objects.create(name = l_name, priority = l_priority, difficulty = l_difficulty, project = lo_project, user = lo_user)
            else:
                l_task = task.objects.create(name = l_name, priority = l_priority, difficulty = l_difficulty, project = lo_project)
        else:
            if l_user != None:
                lo_user = request.user
                l_task = task.objects.create(name = l_name, priority = l_priority, difficulty = l_difficulty, user = lo_user)
            else:
                l_task = task.objects.create(name = l_name, priority = l_priority, difficulty = l_difficulty)
    return main(request)
@login_required
def create_project(request):
    if request.method == 'POST':
        l_name = request.POST.get('name')

        l_project = project.objects.create(name = l_name)

    return main(request)
@login_required
def set_done(request, pk):
     print('hola')
     tarea = get_object_or_404(task, pk=pk)
     tarea.set_done()
     tarea.save()
     return main(request)

@login_required
def set_open(request, pk):
     print('hola')
     tarea = get_object_or_404(task, pk=pk)
     tarea.set_open()
     tarea.save()
     return main(request)

@login_required
def drop(request, pk):
     tarea = get_object_or_404(task, pk=pk)
     tarea.delete()
     return main(request)

def page_not_found(request,exception=None):
    response=render(request,template_name='404.html',)
    response.status_code=404
    return response
#def server_error(request):
 #   response=render(request,template_name='500.html')
  #  response.status_code=500
   # return response


def activo_remove(request, pk):
    post = get_object_or_404(equipo, pk=pk)
    post.delete()
    return redirect('frequently_detail')