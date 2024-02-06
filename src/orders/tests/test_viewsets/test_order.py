from unittest.mock import patch

from rest_framework import status
from rest_framework.reverse import reverse

from orders import serializers
from orders.models import Order
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_order

list_url = 'order-list'
detail_url = 'order-detail'


class OrderListViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.url = reverse(list_url)

    def test_view_is_allowed(self):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_returns_correct_data(self):
        orders = [create_test_order() for i in range(5)]
        expected_data = serializers.OrderSerializer(orders, many=True, context=self.get_fake_context()).data

        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)


class OrderCreateViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.url = reverse(list_url)

    def test_view_is_allowed(self):
        response = self.client.post(self.url, data={})

        self.assertStatusCodeEqual(response, status.HTTP_201_CREATED)

    def test_view_returns_correct_data(self):
        data = {
            'delivery': Order.Delivery.NOVA_POST,
            'delivery_address': 'some delivery address',
            'comment': 'some comment',
        }
        response = self.client.post(self.url, data=data)

        self.assertEqual(Order.objects.count(), 1)

        expected_data = serializers.OrderSerializer(Order.objects.first(), context=self.get_fake_context()).data

        self.assertEqual(response.data, expected_data)


class OrderRetrieveViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.order = create_test_order()
        self.url = reverse(detail_url, args=[self.order.uuid])

    def test_view_is_allowed(self):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_returns_correct_data(self):
        expected_data = serializers.OrderSerializer(self.order, context=self.get_fake_context()).data

        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)


@patch('rest_framework.relations.HyperlinkedRelatedField.to_representation', return_value='mocked_url')
class OrderUpdateViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.order = create_test_order()
        self.url = reverse(detail_url, args=[self.order.uuid])

    def test_view_is_allowed_for_PATCH(self, mock):
        response = self.client.patch(self.url, data={})

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_is_not_allowed_for_PUT(self, mock):
        response = self.client.put(self.url, data={})

        self.assertStatusCodeEqual(response, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_returns_correct_data_for_PATCH(self, mock):
        data = {
            'delivery': Order.Delivery.NOVA_POST,
            'delivery_address': 'some delivery address',
            'comment': 'some comment',
        }
        response = self.client.patch(self.url, data=data)

        self.order.refresh_from_db()
        expected_data = serializers.OrderSerializer(self.order).data

        self.assertEqual(response.data, expected_data)


class OrderDeleteViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.order = create_test_order()
        self.url = reverse(detail_url, args=[self.order.uuid])

    def test_view_is_not_allowed(self):
        response = self.client.delete(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_405_METHOD_NOT_ALLOWED)
