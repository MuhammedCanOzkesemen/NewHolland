from django.contrib import admin
from .models import TractorSeries, TractorModel, SpecGroup, SpecItem

@admin.register(TractorSeries)
class TractorSeriesAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active", "sort_order")
    list_filter = ("is_active",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("sort_order", "name")


class SpecItemInline(admin.TabularInline):
    model = SpecItem
    extra = 0


@admin.register(SpecGroup)
class SpecGroupAdmin(admin.ModelAdmin):
    list_display = ("title", "model", "sort_order")
    list_filter = ("model",)
    search_fields = ("title", "model__name")
    ordering = ("model__series__sort_order", "model__sort_order", "sort_order")


@admin.register(TractorModel)
class TractorModelAdmin(admin.ModelAdmin):
    list_display = ("name", "series", "slug", "is_active", "sort_order")
    list_filter = ("series", "is_active")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("series__sort_order", "sort_order", "name")


@admin.register(SpecItem)
class SpecItemAdmin(admin.ModelAdmin):
    list_display = ("label", "value", "unit", "group", "sort_order")
    list_filter = ("group",)
    search_fields = ("label", "value", "group__title", "group__model__name")
    ordering = ("group__model__series__sort_order", "group__model__sort_order", "group__sort_order", "sort_order")
