from django.http import HttpResponse


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
        return HttpResponse(
            content=f'webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent_payment_failed webhook from Stripe"""
        return HttpResponse(
            content=f'webhook received: {event["type"]}',
            status=200)
