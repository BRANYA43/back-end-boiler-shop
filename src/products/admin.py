from django.contrib import admin

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


class SpecificationInline(admin.StackedInline):
    model = Specification
    fields = ['attributes']
    can_delete = False
    show_change_link = True


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
    fields = ['product', 'attributes']
    search_fields = ['product', 'attributes']


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
