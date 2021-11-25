from django.db import models
from PIL import Image
# from django.forms import ModelForm
# Create your models here.


class House(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rooms = models.CharField(max_length=100)
    baths = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='House')
    """docstring for Post."""

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'House'
        verbose_name_plural = 'Houses'


# class HouseForm(ModelForm):
#     class Meta:
#         model = House
#         fields = ['title', 'location', 'rooms', 'baths', 'image']
