from django.shortcuts import render, render_to_response, get_object_or_404, redirect,HttpResponse
#from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.generic.base import View
from django.template import RequestContext
#from django.views.decorators import csrf
from django.contrib.admin.views.decorators import staff_member_required
from .models import task, project
from .models import equipo
from django.db.models import Q
from .models import equipo
from django.utils import timezone
from django.views.generic import CreateView,TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import equipoModelForm
# Create your views here.


def inicio(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_equipos=equipo.objects.all().count()
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    return render(request, 'gestion/inicio.html',
                  context={'num_equipos':num_equipos,'num_visits':num_visits},
)
@staff_member_required
def counters(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_equipos=equipo.objects.all().count()
    num_na_invima=equipo.objects.filter(invima__exact='na').count()
    num_no_invima=equipo.objects.filter(invima__exact='no').count()
    num_no_factura=equipo.objects.filter(factura__exact='no').count()
    num_na_importacion=equipo.objects.filter(importacion__exact='na').count()
    num_no_importacion=equipo.objects.filter(importacion__exact='no').count()
    num_no_mantenimiento=equipo.objects.filter(mantenimiento__exact='no').count()
    num_na_calibracion=equipo.objects.filter(calibracion__exact='na').count()
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
    posts = equipo.objects.filter(activo__lte=timezone.now()).order_by('activo')
    paginate_by=3
    return render(request, 'gestion/frequently_detail.html', {'posts': posts})
@staff_member_required
def noinvima(request):
    sininvima = equipo.objects.filter(invima__exact='no').order_by('activo')
    return render(request, 'gestion/noinvima.html', {'sininvima': sininvima})
@staff_member_required
def nomanual(request):
    sinmanual = equipo.objects.filter(manual_usuario__exact='no').order_by('activo')
    return render(request, 'gestion/nomanual.html', {'sinmanual': sinmanual})
@staff_member_required
def noaplicainvima(request):
    nainvima = equipo.objects.filter(invima__exact='na').order_by('activo')
    return render(request, 'gestion/noaplicainvima.html', {'nainvima': nainvima})
@staff_member_required
def nofactura(request):
    sinfactura = equipo.objects.filter(factura__exact='no').order_by('activo')
    return render(request, 'gestion/nofactura.html', {'sinfactura': sinfactura})
@staff_member_required
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
@staff_member_required
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
def pdf_view(request):
    with open('gestion/static/media/pdf/mantenimiento.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mantenimiento.pdf.pdf'
        return response
        pdf.closed

@login_required
def pdf_view2(request):
    with open('gestion/static/media/pdf/metrologia.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=metrologia.pdf'
        return response
        pdf.closed


@login_required
def pdf_view3(request):
    with open('gestion/static/media/pdf/inventario.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=inventario.pdf'
        return response
        pdf.closed

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
@staff_member_required
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
@staff_member_required
def create_project(request):
    if request.method == 'POST':
        l_name = request.POST.get('name')

        l_project = project.objects.create(name = l_name)

    return main(request)
@staff_member_required
def set_done(request, pk):
     tarea = get_object_or_404(task, pk=pk)
     tarea.set_done()
     tarea.save()
     return main(request)

@staff_member_required
def set_open(request, pk):
     tarea = get_object_or_404(task, pk=pk)
     tarea.set_open()
     tarea.save()
     return main(request)

@staff_member_required
def drop(request, pk):
     tarea = get_object_or_404(task, pk=pk)
     tarea.delete()
     return main(request)

def page_not_found(request,exception=None):
    response=render(request,template_name='404.html',)
    response.status_code=404
    return response
def server_error(request):
    response=render(request,template_name='500.html')
    response.status_code=500
    return response
