from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import Orderform

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag")
        return redirect(reverse, ('products'))

    order_form = Orderform()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51TfOSzHMPnHHIyxwbTZsWrJucQ0olArIyKhGaZb8LMRQdqJQ5cZFyI6AV5HIGYtEX1z0FThD0l7oXqOmHa6mZL8u00Rc8Ec2s6',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
