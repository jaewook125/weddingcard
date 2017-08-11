from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

import uuid
import os

def get_image_path(instance, filename):
    return os.path.join('mains', "imagecomment_%s" % str(instance), filename)
# 이미지 저장경로 mains/imagemain_(name)/filename

class MainComment(models.Model):
    name = models.CharField(max_length=10)
    image1 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image2 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image3 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image4 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image5 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image6 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image7 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image8 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image9 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image10 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image11 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image12 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image13 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image14 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )

    def __str__(self):
        return self.name

class Comment(models.Model):
    main = models.ForeignKey(MainComment)
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.user
