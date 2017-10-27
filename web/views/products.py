from vasavi_rates.models import Product
from django.template import loader
from django.http import HttpResponse, JsonResponse


def products(request):
    context = {'products': Product.objects.all()}
    template = loader.get_template('web/products.html')
    return HttpResponse(template.render(context, request))


def product_api(request):
    products_object = Product.objects.values()
    product_data = {'products': list(products_object)}
    return JsonResponse(product_data)
