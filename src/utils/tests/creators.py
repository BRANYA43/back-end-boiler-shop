from django.core.files.uploadedfile import SimpleUploadedFile
from faker import Faker

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


def create_test_product(category=None, name=None, slug=None, price=None, **extra_fields):
    if category is None:
        category = create_test_category()
    if name is None:
        name = faker.word()
    if slug is None:
        slug = name + 'slug'
    if price is None:
        price = 1000
    return _create_test_model(Product, category=category, name=name, slug=slug, price=price, **extra_fields)


def create_test_price(product=None, price=None, **extra_fields):
    if product is None:
        product = create_test_product()
    if price is None:
        price = 1000
    return _create_test_model(Price, product=product, price=price, **extra_fields)
