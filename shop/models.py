from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

QualityType = [
    (1, 'Freshly Harvested'),
    (2, 'New Stocks'),
    (3, 'Well Preserved'),
]

ProductType = [
    (1, 'Organic'),
    (2, 'Inorganic'),
    (3, 'Local'),
    (4, 'Foreign')
]

class Products(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=255, decimal_places=2)
    stock = models.IntegerField(default=1)
    measure = models.CharField(max_length=10)
    description = models.TextField()
    quality = models.IntegerField(choices=QualityType, default=3)
    type = models.IntegerField(choices=ProductType, default=3)
    image = models.ImageField(upload_to='productImage', default='LA.png')

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #     if img.height > 700 or img.width > 700:
    #         reseize = (500, 500)
    #         img.thumbnail(reseize)
    #         img.save(self.image.path)

class Bundles(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=255, decimal_places=2)
    stock = models.IntegerField(default=1)
    description = models.TextField()
    quality = models.IntegerField(choices=QualityType, default=3)
    type = models.IntegerField(choices=ProductType, default=3)
    image = models.ImageField(upload_to='bundleImage', default='LA.png')

    def __str__(self):
        return self.name


