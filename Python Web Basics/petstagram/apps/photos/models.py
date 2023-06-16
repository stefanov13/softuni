from django.db import models
from . import validators
from ..pets.models import Pet

class Photo(models.Model):
    photo = models.ImageField(
        validators=(validators.validate_file_size,),
    )

    description = models.TextField(
        max_length=300,
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )

    def __str__(self) -> str:
        return f"{self.photo} - {self.date_of_publication}"