from django.contrib import admin

from .models import PhonesModel


@admin.register(PhonesModel)
class PhonesAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'model_name',
        'brand_name',
        'brand_nationality',
        'manufacturing_country',
        'color',
        'price',
    ]