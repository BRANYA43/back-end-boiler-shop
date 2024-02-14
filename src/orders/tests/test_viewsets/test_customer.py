from rest_framework import status
from rest_framework.reverse import reverse

from utils.tests import CustomTestCase, creators

list_url = 'customer-list'


class OrderViewSetTest(CustomTestCase):
    def setUp(self) -> None:
        self.url = reverse(list_url)
        self.data: dict = {
            'order': creators.create_test_order().uuid,
            'full_name': 'Rick Sanchez',
            'email': 'rick.sanchez@test.com',
            'phone': '000 000 00 00',
        }

    def test_view_is_allowed(self):
        response = self.client.post(self.url, self.data)

        self.assertStatusCodeEqual(response, status.HTTP_201_CREATED)

    def test_view_returns_nothing(self):
        response = self.client.post(self.url, self.data)

        self.assertFalse(response.data)
