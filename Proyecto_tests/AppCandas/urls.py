from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="home"),
    path("motos/", views.motos, name="motos"),
    path("repuestos", views.repuestos, name="repuestos"),
    path("sucursales", views.sucursales, name="sucursales"),
    path("", views.inicio, name="ingresar"),
    path("", views.inicio, name="crear_cuenta"),
    path("motos/ver_motos/", views.ver_motos, name="base_motos"),
    path("motos/alta_moto/", views.moto_formulario, name="alta_moto"),
    path("motos/buscar_moto/", views.buscar_moto, name="consulta_moto"),
    path("repuestos/ver_repuestos/", views.ver_repuestos, name="base_repuestos"),
    path("repuestos/alta_repuesto/", views.repuesto_formulario, name="alta_repuesto"),
    path("repuestos/buscar_repuesto/", views.buscar_repuesto, name="consulta_repuesto"),
    path("sucursales/ver_sucursales/", views.ver_sucursales, name="base_sucursales"),
    path("sucursales/alta_sucursal/", views.sucursal_formulario, name="alta_sucursal"),
    path("sucursales/buscar_sucursal/", views.buscar_sucursal, name="consulta_sucursal"),
    path("buscar_m/", views.buscar_m, name="buscar_m"),
    path("buscar_rep/", views.buscar_rep, name="buscar_rep"),
    path("buscar_s/", views.buscar_s, name="buscar_s"),
    path("eliminar_moto/<int:id>", views.eliminar_moto, name="eliminar_moto"),
    path("eliminar_repuesto/<int:id>", views.eliminar_repuesto, name="eliminar_repuesto"),
    path("eliminar_sucursal/<int:id>", views.eliminar_sucursal, name="eliminar_sucursal"),
    path("editar_moto/<int:id>/", views.editar_moto, name="editar_moto"),
    path("editar_repuesto/<int:id>/", views.editar_repuesto, name="editar_repuesto"),
    path("editar_sucursal/<int:id>/", views.editar_sucursal, name="editar_sucursal"),
    path("login", views.login_request , name="ingresar"),
    path("register", views.register , name="crear_cuenta"),
    path("logut", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("editar_perfil", views.editar_perfil, name="editar_perfil")
]