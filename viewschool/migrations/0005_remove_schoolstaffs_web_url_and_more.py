# Generated by Django 4.1.7 on 2024-09-23 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewschool', '0004_abilitypupils_image_pupil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolstaffs',
            name='web_url',
        ),
        migrations.AlterField(
            model_name='schoolstaffs',
            name='person',
            field=models.CharField(help_text='Masalan: 81-maktab direktori Oloviddin Ochilov', max_length=80, verbose_name="Ko'proq ma'lumot: "),
        ),
    ]
