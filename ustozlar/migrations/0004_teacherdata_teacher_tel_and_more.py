# Generated by Django 4.1.7 on 2023-03-01 12:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ustozlar', '0003_alter_teacherdata_teacher_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherdata',
            name='teacher_tel',
            field=models.CharField(default=django.utils.timezone.now, help_text="Iltimos o'qituvchining telefon raqamini kiriting (shart !)", max_length=50, verbose_name="O'qituvchi telefon raqami: (qo'yish shart)"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacherdata',
            name='teacher_img',
            field=models.ImageField(help_text="O'qituvchining rasmini qo'ying", upload_to='images/'),
        ),
    ]
