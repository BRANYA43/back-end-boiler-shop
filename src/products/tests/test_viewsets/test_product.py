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

    def test_view_filters_product_by_name(self):
        for name in ['p1', 'p2', 'p3']:
            creators.create_test_product(name=name)

        expected_data = self.serializer_class(Product.objects.filter(name='p2'), many=True).data
        response = self.client.get(self.url, {'names': 'p2'})

        self.assertEqual(response.data, expected_data)

    def test_view_filter_product_by_some_names(self):
        for name in ['p1', 'p2', 'p3', 'p4', 'p5']:
            creators.create_test_product(name=name)

        names = 'p2, p3, p4'

        expected_data = self.serializer_class(Product.objects.filter(name__in=names.split(', ')), many=True).data
        response = self.client.get(self.url, {'names': names})

        self.assertEqual(response.data, expected_data)

    def test_view_filter_product_by_category(self):
        categories = [creators.create_test_category(name=name) for name in ['c1', 'c2', 'c3']]
        for category in categories:
            if category.name == 'c2':
                creators.create_test_product(category=category)
            creators.create_test_product(category=category)

        expected_data = self.serializer_class(Product.objects.filter(category__name='c2'), many=True).data
        response = self.client.get(self.url, {'category': 'c2'})

        self.assertEqual(response.data, expected_data)

    def test_view_filters_product_by_attribute(self):
        name_value = {f'n{i}': f'v{i}' for i in range(1, 4)}
        attributes = [creators.create_test_attribute(name, value) for name, value in name_value.items()]
        for attr in attributes:
            product = creators.create_test_product()
            product.specification.all_attributes.set([attr])

        queryset = Product.objects.filter(
            specification__all_attributes__name='n2', specification__all_attributes__value='v2'
        )
        expected_data = self.serializer_class(queryset, many=True).data
        response = self.client.get(self.url, {'attributes': 'n2:v2'})

        self.assertEqual(response.data, expected_data)

    def test_view_filters_product_by_some_attributes(self):
        name_value = {f'n{i}': f'v{i}' for i in range(1, 4)}
        attributes = [creators.create_test_attribute(name, value) for name, value in name_value.items()]
        product_1, product_2, product_3 = [creators.create_test_product() for i in range(3)]
        product_1.specification.all_attributes.set([attributes[0], attributes[1]])
        product_2.specification.all_attributes.set([attributes[1], attributes[2]])
        product_3.specification.all_attributes.set([attributes[1], attributes[0]])

        queryset = Product.objects.filter(uuid__in=(product_1.uuid, product_3.uuid))
        expected_data = self.serializer_class(queryset, many=True).data
        response = self.client.get(self.url, {'attributes': 'n1:v1, n2:v2'})

        self.assertEqual(response.data, expected_data)

    def test_view_filter_product_by_price_range(self):
        for price in range(1000, 3001, 1000):
            if price == 2000:
                creators.create_test_product(price=price)
            creators.create_test_product(price=price)

        expected_data = self.serializer_class(Product.objects.filter(prices__value=2000), many=True).data
        response = self.client.get(self.url, {'price_min': 1500, 'price_max': 2500})

        # Sometimes response data and expected data aren't equal, but they have the same product data
        if response.data != expected_data:
            expected_data = expected_data[::-1]

        self.assertEqual(response.data, expected_data)

    def test_view_filter_product_by_price_range_but_filtering_only_latest_prices(self):
        product = creators.create_test_product()
        creators.create_test_price(product, 1000)  # old price
        creators.create_test_price(product, 100)  # latest price

        response = self.client.get(self.url, {'price_min': 1500, 'price_max': 2500})

        self.assertEqual(response.data, [])


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
