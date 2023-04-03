from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Yangilik nomi')
    date = models.DateField(auto_now_add=True)
    body = RichTextField(blank=False, null=False, verbose_name="Yangilik haqida to'liq ma'lumot")
    image_news = models.ImageField(null=False, blank=False, upload_to="images/", verbose_name='Yangilik rasmi', help_text='Iltimos yangilikga rasm yuklashni unutmang !')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = "Yangilik qo'shish"
        verbose_name_plural = "Yangiliklar"