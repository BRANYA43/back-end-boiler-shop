from rest_framework import status
from rest_framework.reverse import reverse

from orders import serializers
from orders.models import Order
from utils.tests import CustomTestCase

list_url = 'order-list'


class OrderCreateViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.url = reverse(list_url)
        self.data = {
            'delivery': Order.Delivery.NOVA_POST,
            'delivery_address': 'some delivery address',
            'comment': 'some comment',
        }

    def test_view_is_allowed(self):
        response = self.client.post(self.url, data=self.data)

        self.assertStatusCodeEqual(response, status.HTTP_201_CREATED)

    def test_view_returns_correct_data(self):
        response = self.client.post(self.url, data=self.data)

        self.assertEqual(Order.objects.count(), 1)

        expected_data = serializers.OrderSerializer(Order.objects.first(), context=self.get_fake_context()).data

        self.assertEqual(response.data, expected_data)
