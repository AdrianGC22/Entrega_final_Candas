from django.shortcuts import render
from AppCandas.models import Moto, Avatar, Repuesto, Sucursal
from django.http import HttpResponse
from django.template import loader
from AppCandas.forms import Moto_formulario, usereditform, Repuesto_formulario, Sucursal_formulario
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        url = avatares[0].imagen.url
    else:
        url = None
    return render(request, "inicio.html", {"url": url})


# Views motos-----------------------------------------------------------

def motos(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        url = avatares[0].imagen.url
    else:
        url = None
    return render(request, "motos.html", {"url": url})
    
def ver_motos(request):
    motos = Moto.objects.all()       
    return render(request , "ver_motos.html", {"motos": motos })

def moto_formulario(request):
    if request.method == "POST":
        mi_formulario = Moto_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            moto = Moto(
                marca=datos["marca"],
                modelo=datos["modelo"],
                estado=datos["estado"],
                año=datos["año"],
                precio=datos["precio"]
            )
            moto.save()
            return render(request, "formulario_alta_moto.html")
    return render(request, "formulario_alta_moto.html")

def buscar_moto(request):
    return render(request, "buscar_moto.html")

def buscar_m(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        motos = Moto.objects.filter(marca__icontains= marca)
        return render( request , "resultado_busqueda_moto.html" , {"motos":motos})
    else:
        return HttpResponse("Ingrese marca") 
       
def eliminar_moto(request, id):
    moto = Moto.objects.get(id=id)
    moto.delete()
    moto = Moto.objects.all()
    return render(request, "motos.html", {"motos":moto})

def editar_moto(request, id):
    moto = Moto.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Moto_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            moto.marca = datos["marca"]
            moto.modelo = datos["modelo"]
            moto.estado = datos["estado"]
            moto.año = datos["año"]
            moto.precio = datos["precio"]
            moto.save()
            moto = Moto.objects.all()
            return render(request, "motos.html", {"motos":moto})
    else:
        mi_formulario = Moto_formulario(initial={"marca":moto.marca, "modelo": moto.modelo, "estado":moto.estado, "año":moto.año, "precio":moto.precio})
    return render(request, "editar_moto.html", {"mi_formulario": mi_formulario, "moto":moto})




# Views repuestos-----------------------------------------------------------

def repuestos(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        url = avatares[0].imagen.url
    else:
        url = None    
    return render(request, "repuestos.html", {"url": url})


def ver_repuestos(request):
    repuestos = Repuesto.objects.all()       
    return render(request , "ver_repuestos.html", {"repuestos": repuestos })

def repuesto_formulario(request):
    if request.method == "POST":
        mi_formulario = Repuesto_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            repuesto = Repuesto(
                item=datos["item"],
                marca=datos["marca"],
                precio=datos["precio"]
            )
            repuesto.save()
            return render(request, "formulario_alta_repuesto.html")
    return render(request, "formulario_alta_repuesto.html")

def buscar_repuesto(request):
    return render(request, "buscar_repuesto.html")

def buscar_rep(request):
    if request.GET["item"]:
        item = request.GET["item"]
        repuestos = Repuesto.objects.filter(item__icontains = item)
        return render(request, "resultado_busqueda_repuesto.html", {"repuestos": repuestos})
    else:
        return HttpResponse("Ingresar item")
    
def eliminar_repuesto(request, id):
    repuesto = Repuesto.objects.get(id=id)
    repuesto.delete()
    repuesto = Repuesto.objects.all()
    return render(request, "repuestos.html", {"repuestos":repuesto})

def editar_repuesto(request, id):
    repuesto = Repuesto.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Repuesto_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            repuesto.item = datos["item"]
            repuesto.marca = datos["marca"]
            repuesto.precio = datos["precio"]
            repuesto.save()
            repuesto = Repuesto.objects.all()
            return render(request, "repuestos.html", {"repuestos":repuesto})
    else:
        mi_formulario = Repuesto_formulario(initial={"item":repuesto.item, "marca": repuesto.marca, "precio":repuesto.precio})
    return render(request, "editar_repuesto.html", {"mi_formulario": mi_formulario, "repuesto":repuesto})





# Views sucursales-----------------------------------------------------------

def sucursales(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        url = avatares[0].imagen.url
    else:
        url = None
    return render(request, "sucursales.html", {"url": url})


def ver_sucursales(request):
    sucursales = Sucursal.objects.all()       
    return render(request , "ver_sucursales.html", {"sucursales": sucursales })

def sucursal_formulario(request):
    if request.method == "POST":
        mi_formulario = Sucursal_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            sucursal = Sucursal(
                provincia=datos["provincia"],
                localidad=datos["localidad"],
                direccion=datos["direccion"],
                telefono=datos["telefono"],
            )
            sucursal.save()
            return render(request, "formulario_alta_sucursal.html")
    return render(request, "formulario_alta_sucursal.html")

def buscar_sucursal(request):
    return render(request, "buscar_sucursal.html")

def buscar_s(request):
    if request.GET["provincia"]:
        provincia = request.GET["provincia"]
        sucursales = Sucursal.objects.filter(provincia__icontains= provincia)
        return render( request , "resultado_busqueda_sucursal.html" , {"sucursales":sucursales})
    else:
        return HttpResponse("Ingrese provincia") 
       
def eliminar_sucursal(request, id):
    sucursal = Sucursal.objects.get(id=id)
    sucursal.delete()
    sucursal = Sucursal.objects.all()
    return render(request, "sucursales.html", {"sucursales":sucursal})

def editar_sucursal(request, id):
    sucursal = Sucursal.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Sucursal_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            sucursal.provincia = datos["provincia"]
            sucursal.localidad = datos["localidad"]
            sucursal.direccion = datos["direccion"]
            sucursal.telefono = datos["telefono"]
            sucursal.save()
            sucursal = Sucursal.objects.all()
            return render(request, "sucursales.html", {"sucursales":sucursal})
    else:
        mi_formulario = Sucursal_formulario(initial={"provincia":sucursal.provincia, "localidad": sucursal.localidad, "direccion":sucursal.direccion, "telefono":sucursal.telefono})
    return render(request, "editar_sucursal.html", {"mi_formulario": mi_formulario, "sucursal":sucursal})










#-----------------------------------------------------------------------------

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request , user )
                avatares = Avatar.objects.filter(user=request.user.id)
                return render(request, "inicio.html", {"mensaje": f"Bienvenido/a {usuario}", "usuario": usuario, "url": avatares[0].imagen.url})

            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")


    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})




def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "usuario_creado.html")

    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})

def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":
        
        mi_formulario = usereditform(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request , "usuario_editado.html")

    else:
        miFormulario = usereditform(initial={"email":usuario.email})
    
    return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})
