# Register your models here.
from django.contrib import admin
from .models import WashObject, WashBox, WashWasher, Cars, Order, Location


# class StoreToBookInline(admin.TabularInline):
#     model = StoreToBook
#     extra = 1


# @admin.register(WashObject)
# class WashObjectAdmin(admin.ModelAdmin):
#     inlines = [WashObjectInline]


# @admin.register(Book)
# class BookModelAdmin(admin.ModelAdmin):
#     readonly_fields = ['created', 'updated']
#     list_display = ['__str__', ]
#     search_fields = ['name', 'author__full_name']
#     list_filter = ['author']
#     inlines = [StoreToBookInline]
#     filter_horizontal = ('author',)


@admin.register(WashObject)
class WashObjectModelAdmin(admin.ModelAdmin):
    pass


@admin.register(WashBox)
class WashBoxAdmin(admin.ModelAdmin):
    pass


@admin.register(WashWasher)
class WashWasherAdmin(admin.ModelAdmin):
    pass


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
