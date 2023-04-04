from django.db import models
from django.core.validators import MaxLengthValidator

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