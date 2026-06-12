import json
import time
import stripe

from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product, ProductSize


class StripeWH_handler:
    """ handle stripe webhooks """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """" Handle a generic/unknown/unexpected webhook event """
        return HttpResponse(
            content=f'unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent_succeeded webhook from Stripe"""

        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

# Get the Charge object
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        billing_details = stripe_charge.billing_details     # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)  # updated

        # Clean empty strings to None for consistency
        for field_name in ('postcode', 'street_address2', 'county'):
            if locals()[field_name] == "":

                locals()[field_name] = None

# Check whether the order already exists (created by the checkout view)
        order_exists = False
        attempt = 1
        while attempt <= 5:

            try:
                order = Order.objects.get(
                    full_name__iexact=name,
                    email__iexact=email,
                    phone_number__iexact=phone,
                    country__iexact=country,
                    postcode__iexact=post_code,
                    town_or_city__iexact=town_or_city,
                    street_address1__iexact=street_address1,
                    street_address2__iexact=street_address2,
                    county__iexact=county,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
            time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | ' f'SUCCESS: Verified order already in database'), status=200)
        else:
            # Order not found: create it from the webhook as a fallback
            order = None
            try:
                order = Order.objects.create(
                    full_name=name,
                    email=email,
                    phone_number=phone,
                    country=country,
                    postcode=post_code,
                    town_or_city=town_or_city,
                    street_address1=street_address1,
                    street_address2=street_address2,
                    county=county,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for key, quantity in json.loads(bag).items():

                    if ':size-' in key:
                        product_id, size_part = key.split(':size-')
                        size_id = int(size_part)
                        product = Product.objects.get(id=product_id)
                        size = ProductSize.objects.get(
                            id=size_id, product=product)

                        OrderLineItem.objects.create(
                            order=order,
                            product=product,
                            quantity=quantity,
                            product_size=size.label,
                            size_price=size.price,
                        )

                    else:

                        product = Product.objects.get(id=key)

                        OrderLineItem.objects.create(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
            except Exception as e:

                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=(
                f'Webhook received: {event["type"]} | '
                f'SUCCESS: Created order in webhook'
            ), status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent_payment_failed webhook from Stripe"""
        return HttpResponse(
            content=f'webhook received: {event["type"]}',
            status=200)
