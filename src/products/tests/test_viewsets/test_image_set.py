from unittest.mock import patch

from rest_framework import status
from rest_framework.reverse import reverse

from products.serializers import ProductImageSetSerializer
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_product

detail_url = 'productimageset-detail'


@patch('rest_framework.relations.HyperlinkedRelatedField.to_representation', return_value='mocked_url')
class ImageSetRetrieveViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.image_set = create_test_product().image_set
        self.url = reverse(detail_url, args=[self.image_set.uuid])

    def test_view_is_allowed(self, mock):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_returns_correct_data(self, mock):
        expected_data = ProductImageSetSerializer(self.image_set).data
        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)

    def test_view_returns_image_set_data_of_only_displayed_product(self, mock):
        self.image_set.product.is_displayed = False
        self.image_set.product.save()

        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_404_NOT_FOUND)
