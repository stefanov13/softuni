from django.contrib import admin
from . import models

@admin.register(models.Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
    )
