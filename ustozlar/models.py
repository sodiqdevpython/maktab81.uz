from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.

class TeacherData(models.Model):
    teacherfio = models.CharField(max_length=100, verbose_name="O'qituvchi ism, familyasi")
    kasbi = models.CharField(max_length=100, verbose_name="Qaysi fan yoki qanday ish bajarishi", help_text="masalan: direktor yoki O'qituchi (matematika)")
    teacher_info = RichTextField(verbose_name="Qo'shimcha ma'lumotlar")
    teacher_img = models.ImageField(upload_to='images/', null=False, blank=False, help_text="O'qituvchining rasmini qo'ying", verbose_name="O'qituvchi rasmi")
    teacher_tel = models.CharField(max_length=50, verbose_name="O'qituvchi telefon raqami: (qo'yish shart)", help_text="Masalan: +998990327898",)
    def __str__(self):
        return self.teacherfio

    def get_absolute_url(self):
        return reverse('teacher_info')

    class Meta:
        verbose_name = "Yangi ustoz qo'shish"
        verbose_name_plural = "Ustozlar"
        ordering = ['teacherfio']