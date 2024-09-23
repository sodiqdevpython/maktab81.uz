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
    

class SchoolStaffs(models.Model):
    fio = models.CharField(max_length=50, verbose_name="To'liq ismi: ")
    person = models.CharField(max_length=80, verbose_name="Ko'proq ma'lumot: ", help_text="Masalan: 81-maktab direktori Oloviddin Ochilov")
    img_person = models.ImageField(null=False, blank=False, upload_to='images/', verbose_name='Rasm: ')
   
    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Maktab raxbariyati"
        verbose_name_plural = "Maktab raxbariyati"


class AbilityPupils(models.Model):
    fio = models.CharField(max_length=80, verbose_name="To'liq ismi: ")
    text = models.TextField(verbose_name="Qanday yutuqga erishganligi: ", help_text="Qanday yutuqga erishganki saytda turadigan shuni yozing!")
    image_pupil = models.ImageField(upload_to='images/', verbose_name="O'quvchi rasmini kiriting")
    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Iqtidorli o'quvchilar"
        verbose_name_plural = "Iqtidorli o'quvchilar"