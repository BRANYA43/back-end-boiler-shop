from rest_framework import status
from rest_framework.reverse import reverse

from orders.models import Customer
from orders.serializers import CustomerSerializer
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_order

list_url = 'customer-list'


class CustomerCreateViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.url = reverse(list_url)
        self.data = {
            'order': create_test_order().uuid,
            'full_name': 'Rick Sanchez',
            'email': 'rick.sanchez@test.com',
            'phone': '+38 000 000 00 00',
        }

    def test_view_is_allowed(self):
        response = self.client.post(self.url, data=self.data)

        self.assertStatusCodeEqual(response, status.HTTP_201_CREATED)

    def test_view_returns_correct_data(self):
        response = self.client.post(self.url, data=self.data)

        self.assertEqual(Customer.objects.count(), 1)

        customer = Customer.objects.first()
        expected_data = CustomerSerializer(instance=customer).data

        self.assertEqual(response.data, expected_data)
