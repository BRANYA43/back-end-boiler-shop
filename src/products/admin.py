from django.contrib import admin

from products.models import Category, Product, Specification


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    fields = ['product', 'attributes']
    search_fields = ['product', 'attributes']


class SpecificationInline(admin.StackedInline):
    model = Specification
    fields = ['attributes']
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
    readonly_fields = ['total_grade', 'updated', 'created']
    search_fields = ['name', 'slug', 'description']
    list_filter = ['category', 'stock', 'is_displayed']
    inlines = [SpecificationInline]

    def total_grade(self, instance):
        return str(instance.total_grade)


class InlineCategory(admin.TabularInline):
    model = Category
    fields = ['uuid', 'name']
    readonly_fields = ['uuid']
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_parent_category', 'is_sub_category']
    fields = ['uuid', 'name', 'parent']
    readonly_fields = ['uuid']
    search_fields = ['name']
    ordering = ['parent', 'name']
    inlines = [InlineCategory]

    @staticmethod
    def is_parent_category(instance: Category):
        return instance.is_parent_category

    @staticmethod
    def is_sub_category(instance: Category):
        return instance.is_sub_category
