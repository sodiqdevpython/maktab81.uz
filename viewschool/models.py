from django.db import models

# Create your models here.

class SchoolMap(models.Model):
    title = models.CharField(max_length=50, verbose_name="Joy nomini kiriting: ")
    img_location = models.ImageField(null=False, blank=False, upload_to='images/', verbose_name='Joyning rasmini kiriting')
    url_location = models.URLField(verbose_name='Silkani kiriting')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Maktabning 360° ko'rinishini qo'shish"
        verbose_name_plural = "Maktab ko'rinishi 360 °"