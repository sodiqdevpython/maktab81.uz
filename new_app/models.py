from django.db import models

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