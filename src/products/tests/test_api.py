from unittest.mock import patch

from django.urls import NoReverseMatch
from rest_framework import status
from rest_framework.reverse import reverse

from products.models import Category
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_category


class CategoryViewSetTest(CustomTestCase):
    def setUp(self) -> None:
        self.url_names = {
            'list': 'products:category-list',
            'retrieve': 'products:category-detail',
            'create': 'products:category-create',
            'update': 'products:category-update',
            'delete': 'products:category-delete',
        }

    @patch('rest_framework.relations.HyperlinkedRelatedField.to_representation', return_value='mocked_url')
    def test_list_view_returns_category_list(self, mock):
        url = reverse(self.url_names['list'])
        for i in range(3):
            create_test_category()
        expected_category_names = [category.name for category in Category.objects.all()]
        response = self.client.get(url)
        category_names = [category.get('name') for category in response.data]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual(category_names, expected_category_names)

    @patch('rest_framework.relations.HyperlinkedRelatedField.to_representation', return_value='mocked_url')
    def test_retrieve_view_returns_category(self, mock):
        category = create_test_category()
        url = reverse(self.url_names['retrieve'], args=[category.uuid])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), category.name)

    def test_create_view_is_none(self):
        with self.assertRaises(NoReverseMatch):
            reverse('product:category-create')

    def test_update_view_is_none(self):
        with self.assertRaises(NoReverseMatch):
            reverse('product:category-update')

    def test_delete_view_is_none(self):
        with self.assertRaises(NoReverseMatch):
            reverse('product:category-delete')
