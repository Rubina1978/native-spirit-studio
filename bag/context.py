from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, ProductSize


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_key, quantity in bag.items():
        if ':' in str(item_key):
            pid, size_token = str(item_key).split(':', 1)
            size_id = size_token.replace('size-', '')
        else:
            pid = item_key
            size_id = None
            
    # Initial modification developed with assistance of github copilot

        product = get_object_or_404(Product, pk=pid)
        if size_id:
            size = get_object_or_404(ProductSize, pk=size_id, product=product)
            line_price = size.price
        else:
            size = None
            line_price = product.price

        total += quantity * line_price
        product_count += quantity
        bag_items.append({
            'item_id': pid,
            'quantity': quantity,
            'product': product,
            'size': size,
            'unit_price': line_price,
            'total': quantity * line_price,

        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total

    }

    return context
