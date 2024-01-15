from django.db import models

from utils.mixins import CreatedAndUpdatedDateTimeMixin, UUIDMixin


class Stock(models.TextChoices):
    IN_STOCK = 'in_stock', 'In stock'
    OUT_OF_STOCK = 'out_of_stock', 'Out of stock'
    TO_ORDER = 'to_order', 'To order'


class Product(UUIDMixin, CreatedAndUpdatedDateTimeMixin):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.CharField(max_length=20, choices=Stock.choices, default=Stock.IN_STOCK)
    description = models.TextField(blank=True, null=True)
    is_displayed = models.BooleanField(default=True)

    class Meta:
        pass

    def __str__(self):
        return self.name


class Category(UUIDMixin):
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey(
        'self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='sub_categories'
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
        if self.sub_categories.first():
            return True
        return False
