"""
URL configuration for hello_world project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from SpotFinder import views
from hello_world.core import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("",views.login_view,name='login'),
    path("cadastro/", views.cadastro,name='register'),
    path('inicio/',views.pag_inicial,name='home'),
    path('logout/', views.logout_view, name='logout'),
]
'''
urlpatterns=[
   path('/',views.index),
   path('admin/',admin.site.urls),
   path('pginicial/',views.pag_inicial_prelogin),
   path('signin/',views.pag_signin),
   path('signup/',views.pag_signup),
   path('inicio/',views.pag_inicial),
   path('busca/',views.pag_busca),
   path('menu/',views.pag_menu),
   path('ajustes/',views.pag_ajustes),
   path('historico/',views.pag_historico),
   path('filtros/',views.pag_filtros),
   path('favoritos/',views.pag_favoritos),
   path('espacosdisponiveis',views.pag_espdisp),

]'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
