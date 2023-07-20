from django.http import HttpResponse

def hola(request):
    numeros = [int(n) for n in request.GET['numeros'].split(',') ]
    print(numeros)
    numeros_ord = sorted(numeros)
    print(request.GET)
    return HttpResponse(str(numeros_ord))

def verificar(request, nombre, edad):
    if edad < 12:
        mensaje = f'Hola, {nombre} perdon no puede ingresar!!'
    else:
        mensaje = f'Hola,{nombre} Bienvenido =)'

    return HttpResponse(mensaje) 