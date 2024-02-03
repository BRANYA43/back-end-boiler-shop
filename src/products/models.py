from django.core.exceptions import ValidationError
from django.db import models

from utils.mixins import CreatedAndUpdatedDateTimeMixin, ImageSetMixin, UUIDMixin
from utils.models import Attribute, Image


class Price(UUIDMixin):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='prices')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.value}'


class ProductImageSet(ImageSetMixin):
    product = models.OneToOneField('Product', on_delete=models.CASCADE, related_name='image_set')

    def __str__(self):
        return str(self.product)


class Specification(UUIDMixin):
    product = models.OneToOneField('Product', on_delete=models.CASCADE, related_name='specification')
    all_attributes = models.ManyToManyField(Attribute, related_name='specifications', blank=True)
    card_attributes = models.ManyToManyField(Attribute, related_name='_card_specifications', blank=True)
    detail_attributes = models.ManyToManyField(Attribute, related_name='_detail_specifications', blank=True)

    def __str__(self):
        return str(self.product)

    def _check_attributes_for_field(self, field, max_count):
        if field.count() != 0:
            if field.count() > max_count:
                raise ValidationError(f'This field can have maximal {max_count} attributes.')
            if field.difference(self.all_attributes.all()):
                raise ValidationError('This field can have only attributes of all_attributes field.')

    def clean(self):
        self._check_attributes_for_field(self.card_attributes, 3)
        self._check_attributes_for_field(self.detail_attributes, 5)


class Product(UUIDMixin, CreatedAndUpdatedDateTimeMixin):
    class Stock(models.TextChoices):
        IN_STOCK = 'in_stock', 'In stock'
        OUT_OF_STOCK = 'out_of_stock', 'Out of stock'
        TO_ORDER = 'to_order', 'To order'

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
