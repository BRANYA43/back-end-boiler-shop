from django.core.files.uploadedfile import SimpleUploadedFile
from faker import Faker

from orders.models import Order, Customer, OrderProduct
from products.models import Category, Product, Price
from utils.models import Attribute, Image

faker = Faker()


def _create_test_model(model, **fields):
    return model.objects.create(**fields)


def create_test_attribute(name=None, value=None, **extra_fields):
    if name is None:
        name = faker.word()
    if value is None:
        value = faker.word()
    return _create_test_model(Attribute, name=name, value=value, **extra_fields)


def create_test_image(name=None, **extra_fields):
    if name is None:
        name = faker.word()
    image = SimpleUploadedFile('test_image.png', b'', content_type='image/png')
    return _create_test_model(Image, name=name, image=image, **extra_fields)


def create_test_category(name=None, **extra_fields):
    if name is None:
        name = faker.word()
    return _create_test_model(Category, name=name, **extra_fields)


def create_test_product(category=None, name=None, slug=None, **extra_fields):
    if category is None:
        category = create_test_category()
    if name is None:
        name = faker.word()
    if slug is None:
        slug = name + 'slug'
    return _create_test_model(Product, category=category, name=name, slug=slug, **extra_fields)


def create_test_price(product=None, price=None, **extra_fields):
    if product is None:
        product = create_test_product()
    if price is None:
        price = faker.random_number(digits=5)
    return _create_test_model(Price, product=product, price=price, **extra_fields)


def create_test_customer(full_name=None, email=None, phone=None, **extra_fields):
    if full_name is None:
        full_name = faker.name()
    if email is None:
        email = f'{full_name.replace(" ", "_").lower}@example.test'
    if phone is None:
        phone = '+38 ({}) {} {}-{}'.format(*[faker.random_number(digits=i) for i in (3, 3, 2, 2)])
    return _create_test_model(Customer, full_name=full_name, email=email, phone=phone, **extra_fields)


def create_test_order(**extra_fields):
    return _create_test_model(Order, **extra_fields)


def create_test_order_product(order=None, product=None, **extra_fields):
    if order is None:
        order = create_test_order()
    if product is None:
        product = create_test_product()
    return _create_test_model(OrderProduct, order=order, product=product, **extra_fields)
