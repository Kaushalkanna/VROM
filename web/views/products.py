from vasavi_rates.models import Product
from django.template import loader
from django.http import HttpResponse


def products(request):
    products_object = Product.objects.all()
    context = {'products': products_object}
    template = loader.get_template('web/products.html')
    return HttpResponse(template.render(context, request))
