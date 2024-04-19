from django.http import HttpResponse

def saludar (request):
    return HttpResponse("<h1>Hola mundo</h1>")
