# Generated by Django 4.1.7 on 2023-03-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0006_remove_mainslider_main_slide'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoreInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_title', models.CharField(max_length=30, verbose_name="Ma'lumot mavzusi: ")),
                ('data_body', models.CharField(max_length=1000, verbose_name="Ma'lumot haida to'liq xabar: ")),
                ('data_image', models.ImageField(upload_to='images/', verbose_name="Ma'lumot haqida rasm kiriting")),
            ],
        ),
    ]
