# Generated by Django 4.1.7 on 2023-02-19 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pupils', models.CharField(max_length=50, verbose_name="O'quvchilar soni")),
                ('teachers', models.CharField(max_length=50, verbose_name="O'qituvchilar soni")),
                ('ishchi', models.CharField(help_text='(maktab direktori, qorovul va boshqa maktabda ishlaydigan hamma)', max_length=50, verbose_name='Jami ishchilar soni')),
            ],
            options={
                'verbose_name': 'Statistika',
                'verbose_name_plural': 'Maktab statistikasi',
            },
        ),
        migrations.CreateModel(
            name='TopWorkers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kasbi', models.CharField(max_length=100, verbose_name='Kasbi masalan: Direktor')),
                ('rasm', models.ImageField(upload_to='images/')),
                ('rector', models.BooleanField(default=False, help_text="Agar direktor bo'lsa to'g'ri belgisini bosing", verbose_name='Direktor')),
                ('malumot', models.CharField(help_text='Masalan: 81-maktab direktori Oloviddin Ochilov', max_length=100, verbose_name="Ko'proq ma'lumot")),
                ('url_person', models.URLField(help_text="Agar ushbu odamning veb sahifasi yo'q bo'lsa tashlab keting", verbose_name='Ushbu odamning veb sayt manzilini kiriting')),
            ],
            options={
                'verbose_name': 'Yuqori lavozimdagi ishchi',
                'verbose_name_plural': 'Yuqori lavozimdagilar',
            },
        ),
    ]
