from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>soy el index de la app2</h2>")

def saludo(request):
    html="""
    <h1> soy la pagina 1 de la app2</h1>
    <a href="/app2/index">Volver</a>"""
    return HttpResponse(html)