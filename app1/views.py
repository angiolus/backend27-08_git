from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    html="""
    <h1>Soy el index de la app1</h1>
    <h2>Hola!</h2>
    """
    return HttpResponse(html)


def helou(request):
    html="""
    <h1 style="color:red">vamo a jugar pokelol</h1>
    <h2>zi o k</h2>"""
    return HttpResponse(html)