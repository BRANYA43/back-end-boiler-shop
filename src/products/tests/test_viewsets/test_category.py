from rest_framework import status
from rest_framework.reverse import reverse

from products.serializers import CategorySerializer
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_category

list_url = 'category-list'
detail_url = 'category-detail'


class CategoryListViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.url = reverse(list_url)

    def test_view_is_allowed(self):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_returns_correct_data(self):
        categories = [create_test_category() for i in range(3)]
        expected_data = CategorySerializer(categories, many=True, context=self.get_fake_context()).data

        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)


class CategoryRetrieveViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.category = create_test_category()
        self.url = reverse(detail_url, args=[self.category.uuid])

    def test_view_is_allowed(self):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_returns_correct_data(self):
        expected_data = CategorySerializer(self.category, context=self.get_fake_context()).data

        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)
