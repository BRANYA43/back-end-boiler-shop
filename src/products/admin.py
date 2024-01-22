from django.contrib import admin

from products.models import Category, Product, ProductImageSet, Specification, Price


class PriceInline(admin.TabularInline):
    model = Price
    fields = ['uuid', 'price', 'created']
    readonly_fields = ['uuid', 'created']
    show_change_link = True
    extra = 1


class PriceAdmin(admin.ModelAdmin):
    fields = ['product', 'price', 'created']
    search_fields = ['product', 'price']
    ordering = ['-created']


@admin.register(ProductImageSet)
class ProductImageSetAdmin(admin.ModelAdmin):
    fields = ['product', 'images']
    search_fields = ['product', 'images']


class ProductImageSetInline(admin.StackedInline):
    model = ProductImageSet
    fields = ['uuid', 'images']
    readonly_fields = ['uuid']
    can_delete = False


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    fields = ['product', 'attributes']
    search_fields = ['product', 'attributes']


class SpecificationInline(admin.StackedInline):
    model = Specification
    fields = ['uuid', 'attributes']
    readonly_fields = ['uuid']
    can_delete = False


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
    fields = ['uuid', 'name', 'image']
    readonly_fields = ['uuid']
    extra = 1


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
