from django.http import HttpResponse
from django.template import loader

def index(request):
    saludo = "hola"
    template = loader.get_template('libro_diario/index.html')
    context = {
        'saludo': saludo,
    }
    return HttpResponse(template.render(context, request))
