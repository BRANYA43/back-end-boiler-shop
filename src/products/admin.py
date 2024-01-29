from django.contrib import admin
from django import forms

from products.models import Category, Product, ProductImageSet, Specification, Price


class PriceInline(admin.TabularInline):
    model = Price
    fields = ['price', 'created']
    readonly_fields = ['created']
    show_change_link = True
    extra = 1
    ordering = ['-created']

    def has_change_permission(self, request, obj=None):
        return False


class ProductImageSetInline(admin.StackedInline):
    model = ProductImageSet
    fields = ['images']
    can_delete = False
    show_change_link = True


class SpecificationInlineFormSet(forms.models.BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields['card_attributes'].queryset = form.instance.all_attributes
        form.fields['detail_attributes'].queryset = form.instance.all_attributes


class SpecificationInline(admin.StackedInline):
    model = Specification
    fields = ['all_attributes', 'card_attributes', 'detail_attributes']
    can_delete = False
    show_change_link = True
    filter_horizontal = ['all_attributes', 'card_attributes', 'detail_attributes']
    formset = SpecificationInlineFormSet


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['product', 'price', 'created']
    fields = ['product', 'price', 'created']
    search_fields = ['product', 'price']
    readonly_fields = ['created']
    ordering = ['-created']

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(ProductImageSet)
class ProductImageSetAdmin(admin.ModelAdmin):
    fields = ['product', 'images']
    search_fields = ['product', 'images']


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    fields = ['product', 'all_attributes', 'card_attributes', 'detail_attributes']
    search_fields = ['product', 'all_attributes']
    filter_horizontal = ['all_attributes', 'card_attributes', 'detail_attributes']

    def get_object(self, request, object_id, from_field=None):
        obj = super().get_object(request, object_id, from_field)
        request.report_obj = obj
        return obj

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name in ('card_attributes', 'detail_attributes'):
            kwargs['queryset'] = request.report_obj.all_attributes
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'is_displayed', 'stock', 'updated', 'created']
    fields = [
        'category',
        'total_grade',
        'name',
        'slug',
        'price',
        'stock',
        'description',
        'is_displayed',
        'updated',
        'created',
    ]
    prepopulated_fields = {'slug': ['name']}
    readonly_fields = ['price', 'total_grade', 'updated', 'created']
    search_fields = ['name', 'slug', 'description']
    list_filter = ['category', 'stock', 'is_displayed']
    inlines = [SpecificationInline, ProductImageSetInline, PriceInline]

    def total_grade(self, instance):
        return str(instance.total_grade)

    def price(self, instance):
        return str(instance.price.price)


class InlineCategory(admin.TabularInline):
    model = Category
    fields = ['name', 'image']
    extra = 1
    show_change_link = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_parent_category', 'is_sub_category']
    fields = ['name', 'parent', 'image']
    search_fields = ['name']
    ordering = ['parent', 'name']
    inlines = [InlineCategory]

    @staticmethod
    def is_parent_category(instance: Category):
        return instance.is_parent_category

    @staticmethod
    def is_sub_category(instance: Category):
        return instance.is_sub_category
