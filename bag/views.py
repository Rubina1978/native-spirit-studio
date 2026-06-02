from django.shortcuts import render, redirect, get_object_or_404
from products.models import ProductSize

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag.html')

# modified with github copilot assistance to include size choice on items


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    size_id = request.POST.get('size_id')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if size_id:
        size = get_object_or_404(ProductSize, pk=size_id, product_id=item_id)
        key = f"{item_id}:size-{size.id}"
    else:
        size = None
        key = str(item_id)

    if key in bag:
        bag[key] += quantity
    else:
        bag[key] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)
