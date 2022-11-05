from django.db import models
from django.core.validators import MinLengthValidator
from petstagram.accounts.models import PetstagramUser
from petstagram.photos.validators import validate_image_size
from petstagram.pets.models import Pet


class Photo(models.Model):
    photo = models.ImageField(upload_to='images', validators=(validate_image_size,))
    description = models.TextField(max_length=300, validators=(MinLengthValidator(10),), blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pet = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)
    user = models.ForeignKey(to=PetstagramUser, on_delete=models.CASCADE)
