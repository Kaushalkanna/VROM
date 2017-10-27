from vasavi_rates.models import Product
from django.template import loader
from django.http import HttpResponse, JsonResponse


def products(request):
    context = {'products': Product.objects.all()}
    template = loader.get_template('web/products.html')
    return HttpResponse(template.render(context, request))


def product_api(request):
    serialized_data = serialize_data(list(Product.objects.values_list()))
    product_data = {'products': serialized_data}
    return JsonResponse(product_data)


def serialize_data(data_object):
    serialized_list = []
    for lst in data_object:
        serialized_list.append(
            {
                'product_name': lst[1],
                'product_rate': lst[2],
                'bag_weight': lst[3],
                'product_pub_date': lst[4]
            }
        )
    return serialized_list
