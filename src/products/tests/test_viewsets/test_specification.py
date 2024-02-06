from rest_framework import status
from rest_framework.reverse import reverse

from products.serializers import SpecificationSerializer
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_product

detail_url = 'specification-detail'


class SpecificationRetrieveViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.specification = create_test_product().specification
        self.url = reverse(detail_url, args=[self.specification.uuid])

    def test_view_is_allowed(self):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_returns_correct_data(self):
        expected_data = SpecificationSerializer(self.specification, context=self.get_fake_context()).data
        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)

    def test_view_returns_specification_data_of_only_displayed_product(self):
        self.specification.product.is_displayed = False
        self.specification.product.save()

        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_404_NOT_FOUND)
