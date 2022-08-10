
from django.http import HttpResponse

# Request: Para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP.

# Esto es una vista
def bienvenida(request): # Pasamos un objeto de tipo request como primer argumento
    return HttpResponse("BIenvenido a esta página de Emmanuel")

def bienvenidaRojo(request): # Pasamos un objeto de tipo request como primer argumento
    return HttpResponse("<p style= 'color: red;'>BIenvenido a esta página de Emmanuel</p>")