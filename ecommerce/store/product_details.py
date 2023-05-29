from django.db.models import Max, Min
from .models import Product


def get_filters(request):
    min_max_price = Product.objects.aggregate(Min('price'), Max('price'))
    print(min_max_price)

    data = {
        'minmaxprice': min_max_price

    }

    return data