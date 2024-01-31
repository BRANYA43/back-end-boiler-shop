from unittest.mock import patch

from rest_framework import status
from rest_framework.reverse import reverse

from products.models import Category
from utils.tests import CustomTestCase
from utils.tests.creators import create_test_category


class CategoryViewSetTest(CustomTestCase):
    def setUp(self) -> None:
        self.data = {'name': 'Test Category'}

    @patch('rest_framework.relations.HyperlinkedRelatedField.to_representation', return_value='mocked_url')
    def test_list_view_returns_category_list(self, mock):
        expected_uuids = [str(category.uuid) for category in (create_test_category() for i in range(3))]

        response = self.client.get(reverse('products:category-list'))
        uuids = [category.get('uuid') for category in response.data]

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)
        self.assertListEqual(uuids, expected_uuids)

    @patch('rest_framework.relations.HyperlinkedRelatedField.to_representation', return_value='mocked_url')
    def test_retrieve_view_returns_category(self, mock):
        category = create_test_category()
        response = self.client.get(reverse('products:category-detail', args=[category.uuid]))

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)
        self.assertEqual(response.data.get('uuid'), str(category.uuid))

    def test_create_view_is_not_allowed(self):
        response = self.client.post(reverse('products:category-list'), data=self.data)

        self.assertStatusCodeEqual(response, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(Category.objects.count(), 0)

    def test_update_view_is_not_allowed(self):
        category = create_test_category(name='Category')
        response = self.client.put(reverse('products:category-detail', args=[category.uuid]), data=self.data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        category.refresh_from_db()

        self.assertNotEqual(category.name, self.data['name'])

    def test_partial_update_view_is_not_allowed(self):
        category = create_test_category(name='Category')
        response = self.client.put(reverse('products:category-detail', args=[category.uuid]), data=self.data)

        self.assertStatusCodeEqual(response, status.HTTP_405_METHOD_NOT_ALLOWED)

        category.refresh_from_db()

        self.assertNotEqual(category.name, self.data['name'])

    def test_delete_view_is_not_allowed(self):
        category = create_test_category(name='Category')
        response = self.client.delete(reverse('products:category-detail', args=[category.uuid]))

        self.assertStatusCodeEqual(response, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(Category.objects.count(), 1)
