from rest_framework import status
from rest_framework.reverse import reverse

from orders import serializers
from orders.models import OrderProduct
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_product, create_test_order

list_url = 'orderproduct-list'


class OrderProductCreateViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.url = reverse(list_url)
        self.data = {
            'order': create_test_order().uuid,
            'product': create_test_product(price=1000).uuid,
        }

    def test_view_is_allowed(self):
        response = self.client.post(self.url, data=self.data)

        self.assertStatusCodeEqual(response, status.HTTP_201_CREATED)

    def test_view_returns_correct_data(self):
        response = self.client.post(self.url, data=self.data)

        self.assertEqual(OrderProduct.objects.count(), 1)

        expected_data = serializers.OrderProductSerializer(
            OrderProduct.objects.first(), context=self.get_fake_context()
        ).data

        self.assertEqual(response.data, expected_data)
