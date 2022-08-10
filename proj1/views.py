
from django.shortcuts import render

# Request: Para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP.

# Esto es una vista
def homepage(request):
    return render(request, "homepage.html")
