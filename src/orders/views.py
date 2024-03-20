from django.conf import settings
from django.template.loader import render_to_string
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives

from orders import serializers


class OrderSetViewSet(viewsets.ViewSet):
    serializer_class = serializers.OrderSetCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        self.send_message_about_order(data)
        return Response(status=status.HTTP_201_CREATED)

    def send_message_about_order(self, data):
        self._send_msg_to_customer(data)
        self._send_msg_to_owner(data)

    def _send_msg_to_customer(self, data):
        order = data['order']
        customer = data['customer']
        context = data
        body = render_to_string('orders/msg_body_of_order_for_customer.html', context)

        email = EmailMultiAlternatives(
            subject=self._get_subject(order.uuid), body=body, from_email=settings.EMAIL_HOST_USER, to=[customer.email]
        )

        email.attach_alternative(body, 'text/html')
        email.send()

    def _send_msg_to_owner(self, data):
        order = data['order']
        context = data
        body = render_to_string('orders/msg_body_of_order_for_owner.html', context)

        email = EmailMultiAlternatives(
            subject=self._get_subject(order.uuid),
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
        )

        email.attach_alternative(body, 'text/html')
        email.send()

    def _get_subject(self, order_uuid):
        return f'Диво Комфорт | Замовлення №{order_uuid}'
