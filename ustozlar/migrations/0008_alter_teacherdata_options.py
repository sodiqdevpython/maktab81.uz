# Generated by Django 4.1.7 on 2023-03-01 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ustozlar', '0007_alter_teacherdata_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacherdata',
            options={'ordering': ['teacherfio'], 'verbose_name': "Yangi ustoz qo'shish", 'verbose_name_plural': 'Ustozlar'},
        ),
    ]
