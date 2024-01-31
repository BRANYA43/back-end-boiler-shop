from unittest.mock import patch

from rest_framework import status
from rest_framework.reverse import reverse

from products.serializers import CategorySerializer
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_category


list_url = 'products:category-list'
detail_url = 'products:category-detail'


@patch('rest_framework.relations.HyperlinkedRelatedField.to_representation', return_value='mocked_url')
class CategoryListViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.url = reverse(list_url)

    def test_view_is_allowed(self, mock):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_returns_correct_data(self, mock):
        categories = [create_test_category() for i in range(3)]
        expected_data = CategorySerializer(categories, many=True).data

        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)


class CategoryCreateViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.url = reverse(list_url)
        self.data = {'name': 'Some Category'}

    def test_view_is_not_allowed(self):
        response = self.client.post(self.url, data=self.data)

        self.assertStatusCodeEqual(response, status.HTTP_405_METHOD_NOT_ALLOWED)


@patch('rest_framework.relations.HyperlinkedRelatedField.to_representation', return_value='mocked_url')
class CategoryRetrieveViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.category = create_test_category()
        self.url = reverse(detail_url, args=[self.category.uuid])

    def test_view_is_allowed(self, mock):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_returns_correct_data(self, mock):
        expected_data = CategorySerializer(self.category).data

        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)


class CategoryUpdateViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.category = create_test_category()
        self.url = reverse(detail_url, args=[self.category.uuid])
        self.data = {'name': 'Some Category'}

    def test_view_is_not_allowed(self):
        response = self.client.put(self.url, data=self.data)
        self.assertStatusCodeEqual(response, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.patch(self.url, data=self.data)
        self.assertStatusCodeEqual(response, status.HTTP_405_METHOD_NOT_ALLOWED)


class CategoryDeleteViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.category = create_test_category()
        self.url = reverse(detail_url, args=[self.category.uuid])

    def test_view_is_not_allowed(self):
        response = self.client.delete(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_405_METHOD_NOT_ALLOWED)
