import uuid
from django.db import models
from django.urls import reverse
# Create your models here.

# class Genre(models.Model):
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4,
#         editable=False
#     )
#     name = models.CharField(max_length=250, unique=True)
#     description = models.TextField(blank=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'Genre'
#         verbose_name_plural = 'Genres'
    
#     def get_absolute_url(self):
#         return reverse('')

class Movie(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=250)
    director = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    date_released = models.DateField(blank=False, null=False)
    cover = models.ImageField(upload_to='covers/', blank=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', args=[str(self.id)])