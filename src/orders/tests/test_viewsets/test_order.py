from rest_framework import status
from rest_framework.reverse import reverse

from orders.models import Order
from utils.tests import CustomTestCase

list_url = 'order-list'


class OrderViewSetTest(CustomTestCase):
    def setUp(self) -> None:
        self.url = reverse(list_url)
        self.data: dict = {}

    def test_view_is_allowed(self):
        response = self.client.post(self.url, self.data)

        self.assertStatusCodeEqual(response, status.HTTP_201_CREATED)

    def test_view_returns_only_order_uuid(self):
        response = self.client.post(self.url, self.data)
        order = Order.objects.first()

        self.assertEqual(response.data, {'uuid': str(order.uuid)})
