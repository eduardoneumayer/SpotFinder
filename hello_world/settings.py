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