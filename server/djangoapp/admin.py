from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class
class CarModelInline(admin.TabularInline):  # Use TabularInline for a table-like display
    model = CarModel
    extra = 1  # Number of extra empty forms displayed
    
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'dealer_id', 'car_type', 'year')  # Corrected to use car_type
    list_filter = ('car_type', 'year', 'car_make')  # Corrected to use car_type
    search_fields = ('name', 'car_make__name')  # Enable search by car model or make

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'country_of_origin')
    search_fields = ('name',)
    inlines = [CarModelInline]  # Link CarModelInline for managing CarModel inside CarMake

# Register models
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
