from .models import *

from django.contrib import admin


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Branch)
class WashObjectModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarsAdmin(admin.ModelAdmin):
    pass
    # fieldsets = [
    #         (None, {'fields': ['cars_model']}),
    #         ('Date information', {'fields': ['cars_number']})]


admin.site.register([WashType, Location, Coupon, CarType])

# @admin.register(Student)
# class StudentObjectModelAdmin(admin.ModelAdmin):
#     pass


# class StoreToBookInline(admin.TabularInline):
#     model = StoreToBook
#     extra = 1


# @admin.register(Branch)
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

# ეს უფრო მარტივი რატომ არაა:
# admin.site.register(Question)
