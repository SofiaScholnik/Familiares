from django.shortcuts import render

from MiApp.models import Familiares
# Create your views here.

def mostrar_familiares(request):

    a1 = Familiares(nombre='Florencia', apellido= 'Vergara Rossi', edad=50, cumpleanios='1972-05-09')
    a2 = Familiares(nombre='Mercedes', apellido= 'Vergara Rossi', edad=33, cumpleanios='1989-06-17')
    a3 = Familiares(nombre='Valentina', apellido= 'Vergara Rossi', edad=19, cumpleanios='2003-03-04')
    a4 = Familiares(nombre='Juan', apellido= 'Vergara Rossi', edad=15, cumpleanios='2007-08-09')

    return render(request, 'MiApp/familiares.html', {'familiares' :[a1, a2, a3, a4]})
