from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_handler

import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """ listen for webhooks from Stripe"""
    # setup

    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # invalid payload
        print(f'Webhook payload error: {e}')
        return HttpResponse(content=e, status=400)
    except stripe.error.SignatureVerificationError as e:
        # invalid signature
        print(f'Webhook signature error: {e}')
        print(
            f'Loaded webhook secret: {wh_secret[:12]}...{wh_secret[-12:]}'
        )
        print(f'Stripe signature header exists: {bool(sig_header)}')
        return HttpResponse(content=e, status=400)
    except Exception as e:
        print(f'Webhook error: {e}')
        return HttpResponse(content=e, status=400)

    # Set up a webhook handler
    handler = StripeWH_handler(request)

    # Map webhook events to relevant handler function
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': (
            handler.handle_payment_intent_payment_failed
        ),
    }
    # Get the webhook type from Stripe
    event_type = event.type
    # If there is a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
