from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import QuerySet
from django.utils.translation import gettext as _
from django.utils.translation import ngettext

from utils.mixins import CreatedAndUpdatedDateTimeMixin, ImageSetMixin, UUIDMixin
from utils.models import Attribute, Image


class Price(UUIDMixin):
    product = models.ForeignKey(
        to='Product', on_delete=models.CASCADE, related_name='prices', verbose_name=_('Product')
    )
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Value'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Date'))

    class Meta:
        verbose_name = _('Price')
        verbose_name_plural = _('Prices')

    def __str__(self):
        return f'{self.product}:{self.value}'


class ProductImageSet(ImageSetMixin):
    product = models.OneToOneField(
        to='Product',
        on_delete=models.CASCADE,
        related_name='image_set',
        verbose_name=_('Image Set'),
    )

    class Meta:
        verbose_name = _('Product Image Set')
        verbose_name_plural = _('Product Image Sets')

    def __str__(self):
        return str(self.product)


class Specification(UUIDMixin):
    product = models.OneToOneField(
        to='Product',
        on_delete=models.CASCADE,
        related_name='specification',
        verbose_name=_('Product'),
    )
    all_attributes = models.ManyToManyField(
        to=Attribute,
        related_name='specifications',
        blank=True,
        verbose_name=_('All Characteristics'),
    )
    card_attributes = models.ManyToManyField(
        to=Attribute,
        related_name='_card_specifications',
        blank=True,
        verbose_name=_('Characteristics of Card'),
    )
    detail_attributes = models.ManyToManyField(
        to=Attribute,
        related_name='_detail_specifications',
        blank=True,
        verbose_name=_('Characteristic of Detail Page'),
    )

    class Meta:
        verbose_name = _('Specification')
        verbose_name_plural = _('Specifications')

    def __str__(self):
        return str(self.product)

    def _validate_max_attribute_count(self, attributes: QuerySet, max: int):
        message = ngettext(
            'This field can have maximal {max} attribute.', 'This field can have maximal {max} attributes.', max
        )
        code = 'invalid_attribute_count'
        if 0 < attributes.count() > max:
            raise ValidationError(message, code, params={'max': max})

    def _validate_attributes_is_in_all_attributes(self, attributes: QuerySet):
        message = _('This field can have only attributes of all_attributes field.')
        code = 'invalid_attribute'
        if 0 < attributes.count() and attributes.difference(self.all_attributes.all()):
            raise ValidationError(message, code)

    def clean_card_attributes(self):
        self._validate_max_attribute_count(self.card_attributes, 3)
        self._validate_attributes_is_in_all_attributes(self.card_attributes)

    def clean_detail_attributes(self):
        self._validate_max_attribute_count(self.detail_attributes, 5)
        self._validate_attributes_is_in_all_attributes(self.detail_attributes)

    def clean(self):
        self.clean_card_attributes()
        self.clean_detail_attributes()


class Product(UUIDMixin, CreatedAndUpdatedDateTimeMixin):
    class Stock(models.TextChoices):
        IN_STOCK = 'in_stock', _('In stock')
        OUT_OF_STOCK = 'out_of_stock', _('Out of stock')
        TO_ORDER = 'to_order', _('To order')

    name = models.CharField(max_length=50, verbose_name=_('Title'))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_('Slug'))
    category = models.ForeignKey(
        to='Category',
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name=_('Category'),
    )
    stock = models.CharField(
        max_length=20,
        choices=Stock.choices,
        default=Stock.IN_STOCK,
        verbose_name=_('Stock'),
    )
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    is_displayed = models.BooleanField(default=True, verbose_name=_('Is Displayed'))

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name

    @property
    def price(self) -> Price | None:
        if self.prices.exists():
            return self.prices.latest('created')
        return None


class Category(UUIDMixin):
    image = models.ForeignKey(
        to=Image,
        on_delete=models.PROTECT,
        related_name='categories',
        null=True,
        blank=True,
        verbose_name=_('Image'),
    )
    name = models.CharField(max_length=50, unique=True, verbose_name=_('Title'))
    parent = models.ForeignKey(
        to='self',
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='children',
        verbose_name=_('Parent Category'),
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

    @property
    def is_child_category(self):
        if self.parent:
            return True
        return False

    @property
    def is_parent_category(self):
        if self.children.first():
            return True
        return False
