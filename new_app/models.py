from django.db import models
from django.core.validators import MaxLengthValidator

class TopWorkers(models.Model):
    kasbi = models.CharField(max_length=100, verbose_name="Kasbi masalan: Direktor")
    rasm = models.ImageField(null=False, blank=False, upload_to="images/")
    rector = models.BooleanField(default=False, verbose_name='Direktor', help_text="Agar direktor bo'lsa to'g'ri belgisini bosing")
    malumot = models.CharField(max_length=100, verbose_name="Ko'proq ma'lumot", help_text="Masalan: 81-maktab direktori Oloviddin Ochilov")
    url_person = models.URLField(verbose_name="Ushbu odamning veb sayt manzilini kiriting", help_text="Agar ushbu odamning veb sahifasi yo'q bo'lsa tashlab keting")
    def __str__(self):
        return self.malumot

    class Meta:
        verbose_name = "Yuqori lavozimdagi ishchi"
        verbose_name_plural = "Yuqori lavozimdagilar"

class SchoolData(models.Model):
    pupils = models.CharField(max_length=50, verbose_name="O'quvchilar soni")
    teachers = models.CharField(max_length=50, verbose_name="O'qituvchilar soni")
    ishchi = models.CharField(max_length=50, verbose_name="Jami ishchilar soni", help_text="(maktab direktori, qorovul va boshqa maktabda ishlaydigan hamma)")

    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Maktab statistikasi"

class MainSlider(models.Model):
    slide_title = models.CharField(max_length=60, verbose_name="slayd mavzusi: ")
    slide_body = models.CharField(max_length=40, verbose_name="slayd tektstini kiriting: ")
    slide_img = models.ImageField(upload_to='images/', verbose_name="slaydga rasm qo'ying: ")
    def __str__(self):
        return self.slide_title
    class Meta:
        verbose_name = "Slayder qo'shish"
        verbose_name_plural = "Slayder qo'shish"

class MoreInformation(models.Model):
    data_title = models.CharField(max_length=30, verbose_name="Ma'lumot mavzusi: ")
    data_body = models.TextField(verbose_name="Ma'lumot haida to'liq xabar:", validators=[MaxLengthValidator(1000, message="Xato sizning kiritgan ma'lumotlaringiz 1000 ta belgidan oshib ketdi kamaytiring bo'lmasa bu xato sayt dizayniga ta'sir qiladi")])
    data_image = models.ImageField(upload_to='images/', verbose_name="Ma'lumot haqida rasm kiriting")
    def __str__(self):
        return self.data_title
    class Meta:
        verbose_name = "Saytga ma'lumot qo'shish"
        verbose_name_plural = "Sayt ma'lumotlari"