"""QUIRUSTETIC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('gestion/', include('blog.urls'))
"""
from django.contrib import admin
#from django.contrib.auth import LoginView,LogoutView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordResetView
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler403, handler404, handler500


#handler400 = 'gestion.views.bad_request'
#handler403 = 'my_app.views.permission_denied'
handler404 = 'gestion.views.page_not_found'
#handler500 = 'gestion.views.server_error'
#from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    #url(r'^accounts/login/$', auth_views.LoginView, name='login'),
    #url(r'^accounts/logout/$',auth_views.LogoutView, name='logout'),
    #url(r'^password_reset', auth_views.PasswordResetForm , name='password_reset'),
    #url(r'^password_reset/done/$', auth_views.PasswordResetView, name='password_reset_done'),
    #url(r'^password_reset/confirm/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #url(r'^password_reset/complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('', include('gestion.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'Sistema De Gestion Tecnologica'

