from django.conf import settings
from django.core import mail
from rest_framework import status
from rest_framework.reverse import reverse

from orders.models import Order, Customer, OrderProduct
from utils.tests import CustomTestCase, creators


class OrderSetCreateViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.product = creators.create_test_product(price=1000)
        self.url = reverse('orderset-list')
        self.data = {
            'order': {},
            'customer': {
                'full_name': 'Rick Sanchez',
                'email': 'rick.sanchez@test.com',
                'phone': '+38(000) 000 00-00',
            },
            'products': [{'product': self.product.uuid}],
        }

    def test_view_is_allowed(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertStatusCodeEqual(response, status.HTTP_201_CREATED)

    def test_view_doesnt_return_data(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertIsNone(response.data)

    def test_view_create_order(self):
        self.assertEqual(Order.objects.count(), 0)

        self.client.post(self.url, self.data, format='json')

        self.assertEqual(Order.objects.count(), 1)

    def test_view_create_customer(self):
        self.assertEqual(Customer.objects.count(), 0)

        self.client.post(self.url, self.data, format='json')

        self.assertEqual(Customer.objects.count(), 1)

    def test_view_create_product(self):
        self.assertEqual(OrderProduct.objects.count(), 0)

        self.client.post(self.url, self.data, format='json')

        self.assertEqual(OrderProduct.objects.count(), 1)

    def test_view_sends_two_msgs(self):
        self.assertEqual(len(mail.outbox), 0)

        self.client.post(self.url, self.data, format='json')

        self.assertEqual(len(mail.outbox), 2)

    def test_view_sends_msg_for_customer(self):
        self.client.post(self.url, self.data, format='json')
        self.assertTrue([msg for msg in mail.outbox if msg.to[0] == self.data['customer']['email']])

    def test_view_sends_msg_for_owner(self):
        self.client.post(self.url, self.data, format='json')
        self.assertTrue([msg for msg in mail.outbox if msg.to[0] == settings.EMAIL_HOST_USER])
