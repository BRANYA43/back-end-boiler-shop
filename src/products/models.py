from django.db import models

from utils.mixins import CreatedAndUpdatedDateTimeMixin, ImageSetMixin, UUIDMixin
from utils.models import Attribute, Image


class Price(UUIDMixin):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product}: {self.price}'


class ProductImageSet(ImageSetMixin):
    product = models.OneToOneField('Product', on_delete=models.CASCADE, related_name='image_set')

    def __str__(self):
        return str(self.product)


class Specification(UUIDMixin):
    product = models.OneToOneField('Product', on_delete=models.CASCADE, related_name='specification')
    attributes = models.ManyToManyField(Attribute, related_name='specifications', blank=True)

    def __str__(self):
        return str(self.product)


class Stock(models.TextChoices):
    IN_STOCK = 'in_stock', 'In stock'
    OUT_OF_STOCK = 'out_of_stock', 'Out of stock'
    TO_ORDER = 'to_order', 'To order'


class Product(UUIDMixin, CreatedAndUpdatedDateTimeMixin):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='products')
    stock = models.CharField(max_length=20, choices=Stock.choices, default=Stock.IN_STOCK)
    description = models.TextField(blank=True, null=True)
    is_displayed = models.BooleanField(default=True)

    class Meta:
        pass

    def __str__(self):
        return self.name

    @property
    def price(self) -> Price | None:
        if self.prices.exists():
            return self.prices.latest('created')
        return None


class Category(UUIDMixin):
    image = models.ForeignKey(Image, on_delete=models.PROTECT, related_name='categories', null=True, blank=True)
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey(
        'self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='subs'
    )

    def __str__(self):
        return self.name

    @property
    def is_sub_category(self):
        if self.parent:
            return True
        return False

    @property
    def is_parent_category(self):
        if self.subs.first():
            return True
        return False
