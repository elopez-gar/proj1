import ...
from django.http import HttpResponse

# Request: Para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP.

# Esto es una vista
def bienvenidaRojo(request): # Pasamos un objeto de tipo request como primer argumento
    return HttpResponse("<p style= 'color: red;'>Bienvenido a esta página de Emmanuel</p>")
def homepage(request):
    return render_to_response('homepage.html',
        context_instance=RequestContext(request))