from rest_framework import status
from rest_framework.reverse import reverse

from products import serializers
from products.models import Category
from utils.tests import CustomTestCase, creators

list_url = 'category-list'
detail_url = 'category-detail'


class CategoryListViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.url = reverse(list_url)
        self.serializer_class = serializers.CategoryListSerializer

    def test_view_is_allowed(self):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_uses_correct_serializer(self):
        for i in range(3):
            parent = creators.create_test_category()
            creators.create_test_category(parent=parent)
        expected_data = self.serializer_class(Category.objects.all(), many=True).data

        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)


class CategoryRetrieveViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.category = creators.create_test_category()
        self.url = reverse(detail_url, args=[self.category.uuid])
        self.serializer_class = serializers.CategoryDetailSerializer

    def test_view_is_allowed(self):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_uses_correct_serializer(self):
        for i in range(3):
            creators.create_test_category(parent=self.category)
            creators.create_test_product(category=self.category)
        self.category.refresh_from_db()
        expected_data = self.serializer_class(self.category).data

        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)
