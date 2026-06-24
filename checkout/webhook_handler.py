import json

import time

import stripe


from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product, ProductSize
from profiles.models import UserProfile


class StripeWH_handler:

    """ Handle Stripe webhooks """

    def __init__(self, request):

        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):

        """ Handle a generic/unknown/unexpected webhook event """

        return HttpResponse(

            content=f'Unhandled webhook received: {event["type"]}',

            status=200)

    def handle_payment_intent_succeeded(self, event):

        """ Handle the payment_intent.succeeded webhook from Stripe """

        intent = event.data.object

        pid = intent.id

# Metadata may be absent on test-triggered events

        bag = getattr(intent.metadata, 'bag', '')
        save_info = getattr(intent.metadata, 'save_info', None)

# Get the Charge object for billing details and authoritative total

        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

        billing_details = stripe_charge.billing_details

        grand_total = round(stripe_charge.amount / 100, 2)

        # update profile information in save_info
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = billing_details.phone
                profile.default_country = billing_details.address.country
                profile.default_postcode = billing_details.address.postal_code
                profile.default_town_or_city = billing_details.address.city
                profile.default_street_address1 = billing_details.address.line1
                profile.default_street_address2 = billing_details.address.line2
                profile.default_county = billing_details.address.state
                profile.save()

# Option A: read the address from billing details

        address = billing_details.address

        name = billing_details.name or None

        email = billing_details.email or None

        phone = billing_details.phone or None

        country = address.country or None

        postcode = address.postal_code or None

        town_or_city = address.city or None

        street_address1 = address.line1 or None

        street_address2 = address.line2 or None

        county = address.state or None

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

                    postcode__iexact=postcode,

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
            self._send_confirmation_email(order)
            return HttpResponse(

                content=(
                    f'Webhook received: {event["type"]} | '
                    f'SUCCESS: Verified order already in database'

                ),

                status=200)

# Order not found: create it from the webhook as a fallback

        order = None

        try:

            order = Order.objects.create(

                full_name=name,
                user_profile=profile,
                email=email,

                phone_number=phone,

                country=country,

                postcode=postcode,

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

                    size = ProductSize.objects.get(id=size_id, product=product)

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
        self._send_confirmation_email(order)
        return HttpResponse(

            content=(

                f'Webhook received: {event["type"]} | '

                f'SUCCESS: Created order in webhook'

            ),

            status=200)

    def handle_payment_intent_payment_failed(self, event):

        """ Handle the payment_intent.payment_failed webhook from Stripe """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)
