from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Main(models.Model):
    name = models.CharField(max_length=10)
    image = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            format='JPEG',
            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Name(models.Model):
    husband = models.CharField(max_length=10)
    wife = models.CharField(max_length=10)
    content = models.CharField(max_length=500)
