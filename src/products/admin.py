from django.contrib import admin

from products.models import Category


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
