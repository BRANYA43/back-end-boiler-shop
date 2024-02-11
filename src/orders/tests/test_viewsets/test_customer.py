from rest_framework import status
from rest_framework.reverse import reverse

from orders import serializers
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_customer

detail_url = 'customer-detail'


class CustomerRetrieveViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.customer = create_test_customer()
        self.url = reverse(detail_url, args=[self.customer.uuid])

    def test_view_is_allowed(self):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_returns_correct_data(self):
        expected_data = serializers.CustomerSerializer(self.customer, context=self.get_fake_context()).data
        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)


class CustomerUpdateViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.customer = create_test_customer()
        self.url = reverse(detail_url, args=[self.customer.uuid])

    def test_view_is_allowed_for_PATCH(self):
        response = self.client.patch(self.url, data={})

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_is_not_allowed_for_PUT(self):
        response = self.client.put(self.url, data={})

        self.assertStatusCodeEqual(response, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_returns_correct_data(self):
        data = {'full_name': 'Test Full Name', 'phone': '000 000 00 00', 'email': 'test@test.com'}
        response = self.client.patch(self.url, data=data, context=self.get_fake_context())

        self.customer.refresh_from_db()
        expected_data = serializers.CustomerSerializer(self.customer, context=self.get_fake_context()).data

        self.assertEqual(response.data, expected_data)
