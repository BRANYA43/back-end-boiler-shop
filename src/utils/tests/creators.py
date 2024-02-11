from decimal import Decimal

from django.core.files.uploadedfile import SimpleUploadedFile
from faker import Faker

from orders.models import Order, OrderProduct, Customer
from products.models import Category, Product, Price
from utils.models import Attribute, Image

faker = Faker()

price_ = int | float | str | Decimal


def _create_test_model(model, **fields):
    return model.objects.create(**fields)


def _get_count(model) -> int:
    return model.objects.count()


def _get_name(model) -> str:
    return f'{model}-{_get_count(model)}'


def create_test_attribute(name: str = None, value: str = None) -> Attribute:
    """
    Create test attribute.
    If name or value is none, they will be generated.
    :param name: attribute name.
    :param value: attribute value.
    """
    count = _get_count(Attribute)
    if name is None:
        name = _get_name(Attribute)
    if value is None:
        value = str(count)
    return _create_test_model(Attribute, name=name, value=value)


def create_test_image(name: str = None, image: SimpleUploadedFile = None) -> Image:
    """
    Create test image.
    If name or image is none, they will be generated.
    :param name: image name.
    :param image: image data.
    """
    if name is None:
        name = _get_name(Image)
    if image is None:
        image = SimpleUploadedFile(f'{name}.png', b'', content_type='image/png')
    return _create_test_model(Image, name=name, image=image)


def create_test_category(name: str = None, **extra_fields):
    """
    Create test category.
    If name is none, it will be generated.
    :param name: category name.
    :param extra_fields: extra fields of category(image, parent).
    :return:
    """
    if name is None:
        name = _get_name(Category)
    return _create_test_model(Category, name=name, **extra_fields)


def create_test_product(
    category: Category = None, name: str = None, slug: str = None, price: price_ = None, **extra_fields
) -> Product:
    """
    Create test product.
    If category, name or slug is none, they will be generated.
    If price isn't none, price is created for product with value "price".
    :param category: instance of Category.
    :param name: product name.
    :param slug: product slug.
    :param price: price value of instance Price.
    :param extra_fields: extra fields of product(stock, description, is_displayed).
    """
    if category is None:
        category = create_test_category()
    if name is None:
        name = _get_name(Product)
    if slug is None:
        slug = name.replace('-', '_')
    product = _create_test_model(Product, category=category, name=name, slug=slug, **extra_fields)
    if price:
        create_test_price(product, price)
    return product


def create_test_price(product: Product = None, value: price_ = None) -> Price:
    """
    Create test price.
    If product or price is none, they will be generated.
    :param product: instance of Product.
    :param value: value of price
    """
    if product is None:
        product = create_test_product()
    if value is None:
        value = faker.random_number(digits=5)
    return _create_test_model(Price, product=product, value=value)


def create_test_order(**extra_fields) -> Order:
    """
    Create test order.
    :param extra_fields: extra fields of order(delivery, delivery_address, payment, is_paid, status, comment).
    """
    return _create_test_model(Order, **extra_fields)


def create_test_order_product(
    order: Order = None, product: Product = None, price: price_ = None, **extra_fields
) -> OrderProduct:
    """
    Create test order product.
    If order, product or price is none, they will be generated.
    :param order: instance of Order.
    :param product: instance of Product.
    :param price: value of price
    :param extra_fields: extra fields of order product(quantity).
    """
    if order is None:
        order = create_test_order()
    if product is None:
        product = create_test_product(price=price if price else faker.random_number(digits=5))
    return _create_test_model(OrderProduct, order=order, product=product, **extra_fields)


def create_test_customer(order: Order = None, full_name: str = None, email: str = None, phone: str = None) -> Customer:
    """
    Create test customer.
    If order, full name, email or phone is none, they will be generated.
    :param order: instance of Order.
    :param full_name: full name of customer.
    :param email: email of customer.
    :param phone: phone number of customer.
    """
    if order is None:
        order = create_test_order()
    if full_name is None:
        full_name = faker.name()
    if email is None:
        email = '{}@test.com'.format(full_name.lower().replace(' ', '.'))
    if phone is None:
        phone = '+38' + faker.phone_number()
    return _create_test_model(Customer, order=order, full_name=full_name, email=email, phone=phone)
