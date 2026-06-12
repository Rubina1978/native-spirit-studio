from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib import messages
from products.models import ProductSize, Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag.html')


# modified with github copilot assistance to include size choice on items

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size_id = request.POST.get('size_id')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if size_id:
        size = get_object_or_404(ProductSize, pk=size_id, product_id=item_id)
        key = f"{item_id}:size-{size.id}"
        messages.success(request, f'Added {product.name} ({size.label})')

    else:
        size = None
        key = str(item_id)
        messages.success(request, f'Added {product.name} to your bag')

    if key in bag:
        bag[key] += quantity

    else:
        bag[key] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

# with ai help modified adjust and remove item in code to
# fit to my custom ProductSize model


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    size_id = request.POST.get('size_id')
    bag = request.session.get('bag', {})

    if size_id:
        size = get_object_or_404(
            ProductSize,
            pk=size_id,
            product_id=item_id
        )
        key = f"{item_id}:size-{size_id}"
    else:
        key = str(item_id)

    if quantity > 0:
        bag[key] = quantity

        if size_id:
            messages.success(
                request,
                f'Updated quantity of {product.name}({size.label})\
                    to {quantity}'
            )
        else:
            messages.success(
                request,
                f'Updated quantity of {product.name} to {quantity}'
            )

    else:
        bag.pop(key, None)

        messages.success(
            request,
            f'Removed {product.name} from your bag'
        )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        size_id = request.POST.get('size_id')

        if size_id:
            size = get_object_or_404(
                ProductSize,
                pk=size_id,
                product_id=item_id
            )
            key = f"{item_id}:size-{size_id}"

            messages.success(
                request,
                f'Successfully removed {product.name} ({size.label}) \
                from your bag'
            )
        else:
            key = str(item_id)

            messages.success(
                request,
                f'Successfully removed {product.name} from your bag'
            )

        bag.pop(key, None)
        request.session['bag'] = bag

        return HttpResponse(status=200)

    except Exception as e:

        return HttpResponse(content=e, status=500)
