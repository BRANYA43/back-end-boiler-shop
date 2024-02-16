from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _

from products.models import Category, Product, ProductImageSet, Specification, Price


class PriceInline(admin.TabularInline):
    model = Price
    fields = ('value', 'created')
    readonly_fields = ('created',)
    ordering = ('-created',)
    extra = 0
    show_change_link = True
    min_num = 1

    def has_change_permission(self, request, obj=None):
        return False


class ProductImageSetInline(admin.StackedInline):
    model = ProductImageSet
    fields = ('cover_image', 'images')
    filter_horizontal = ('images',)
    can_delete = False
    show_change_link = True


class SpecificationInlineFormSet(forms.models.BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields['card_attributes'].queryset = form.instance.all_attributes
        form.fields['detail_attributes'].queryset = form.instance.all_attributes


class SpecificationInline(admin.StackedInline):
    model = Specification
    fields = ('all_attributes', 'card_attributes', 'detail_attributes')
    filter_horizontal = ('all_attributes', 'card_attributes', 'detail_attributes')
    can_delete = False
    show_change_link = True
    formset = SpecificationInlineFormSet


@admin.action(description=_('Set stock as "in stock"'))
def make_in_stock(modeladmin, request, queryset):
    queryset.update(stock=Product.Stock.IN_STOCK)


@admin.action(description=_('Set stock as "out of stock"'))
def make_out_of_stock(modeladmin, request, queryset):
    queryset.update(stock=Product.Stock.OUT_OF_STOCK)


@admin.action(description=_('Set stock as "to order"'))
def make_to_order(modeladmin, request, queryset):
    queryset.update(stock=Product.Stock.TO_ORDER)


@admin.action(description=_('Switch displaying'))
def switch_displaying(modeladmin, request, queryset):
    for instance in queryset:
        instance.update(is_displayed=not instance.is_displayed)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'stock', 'price', 'is_displayed', 'updated', 'created')
    fields = (
        'category',
        'name',
        'price',
        'stock',
        'description',
        'is_displayed',
        'updated',
        'created',
    )
    readonly_fields = ('price', 'updated', 'created')
    search_fields = (
        'name',
        'description',
        'specification__all_attributes__name',
        'specification__all_attributes__value',
    )
    list_filter = ('category', 'stock', 'is_displayed')
    inlines = [SpecificationInline, ProductImageSetInline, PriceInline]
    actions = [switch_displaying, make_in_stock, make_out_of_stock, make_to_order]


class InlineCategory(admin.TabularInline):
    model = Category
    fields = (
        'name',
        'image',
    )
    extra = 1
    show_change_link = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_parent_category', 'is_child_category')
    fields = ('name', 'parent', 'image')
    search_fields = ('name',)
    ordering = ('parent', 'name')
    inlines = (InlineCategory,)

    @admin.display(boolean=True, description=_('Is parent category'))
    def is_parent_category(self, obj: Category):
        return obj.is_parent_category

    @admin.display(boolean=True, description=_('Is child category'))
    def is_child_category(self, obj: Category):
        return obj.is_child_category
