from django.contrib import admin
from .models import CarMake, CarModel

# Register CarModel inline with CarMake
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of empty forms to display by default

# Register CarModel with custom admin
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')
    search_fields = ('name', 'car_make__name')  # Search by car make name and model name

# Register CarMake with the CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')
    search_fields = ('name',)

# Register the models with the admin site
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
