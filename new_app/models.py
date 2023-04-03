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
    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Maktab statistikasi"

class MoreInformation(models.Model):
    data_title = models.CharField(max_length=30, verbose_name="Ma'lumot mavzusi: ")
    data_body = models.TextField(verbose_name="Ma'lumot haida to'liq xabar:", validators=[MaxLengthValidator(1000, message="Xato sizning kiritgan ma'lumotlaringiz 1000 ta belgidan oshib ketdi kamaytiring bo'lmasa bu xato sayt dizayniga ta'sir qiladi")])
    data_image = models.ImageField(upload_to='images/', verbose_name="Ma'lumot haqida rasm kiriting")
    def __str__(self):
        return self.data_title
    class Meta:
        verbose_name = "Saytga ma'lumot qo'shish"
        verbose_name_plural = "Sayt ma'lumotlari"


class SchoolContact(models.Model):
    school_tel = models.CharField(max_length=50,verbose_name="Maktab telefon raqami: ")
    school_email = models.CharField(max_length=50, verbose_name="Maktab emaili: ")
    school_tme = models.URLField(verbose_name="Telegram url: ", help_text="Bog'lanish uchun telegram manzil url ini kiriting")
    school_youtube = models.URLField(verbose_name="YouTube url: ", help_text="YouTube url manzilini kiriting")
    school_facebook = models.URLField(verbose_name="Facebook url: ", help_text="Facebook url manzilini kiriting")
    school_instagram = models.URLField(verbose_name="Instagram url: ", help_text="Instagram url manzilini kiriting")
    
    def __str__(self):
        return self.school_tel
    
    class Meta:
        verbose_name = "Bog'lanish uchun"
        verbose_name_plural = "Bog'lanish uchun"