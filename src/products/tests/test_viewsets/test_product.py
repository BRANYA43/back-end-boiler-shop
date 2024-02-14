from rest_framework import status
from rest_framework.reverse import reverse


from products import serializers
from products.models import Product
from utils.tests import CustomTestCase, creators

list_url = 'product-list'
detail_url = 'product-detail'


class ProductListViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.url = reverse(list_url)
        self.serializer_class = serializers.ProductListSerializer

    def test_view_is_allowed(self):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_uses_correct_serializer(self):
        attributes = [creators.create_test_attribute() for i in range(3)]
        for price in range(1000, 3001, 1000):
            product = creators.create_test_product(price=price)
            product.specification.all_attributes.set(attributes)
            product.specification.card_attributes.set(attributes)
            product.refresh_from_db()
        expected_data = self.serializer_class(Product.objects.all(), many=True).data

        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)


class ProductRetrieveViewTest(CustomTestCase):
    def setUp(self) -> None:
        self.product = creators.create_test_product(price=1000)
        self.url = reverse(detail_url, args=[self.product.uuid])
        self.serializer_class = serializers.ProductDetailSerializer

    def test_view_is_allowed(self):
        response = self.client.get(self.url)

        self.assertStatusCodeEqual(response, status.HTTP_200_OK)

    def test_view_uses_correct_serializer(self):
        attributes = [creators.create_test_attribute() for i in range(5)]
        self.product.specification.all_attributes.set(attributes)
        self.product.specification.detail_attributes.set(attributes)
        self.product.refresh_from_db()
        expected_data = self.serializer_class(self.product).data

        response = self.client.get(self.url)

        self.assertEqual(response.data, expected_data)
