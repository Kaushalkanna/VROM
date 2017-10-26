from django.template import loader
from django.http import HttpResponse


def homepage(request):
    context = {}
    template = loader.get_template('web/home.html')
    return HttpResponse(template.render(context, request))
