# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # fields = ['end_time', 'status']
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


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(CarType)


admin.site.register(WashType)


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
