# Generated by Django 4.0.4 on 2022-04-26 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام و نام خانوادگي')),
                ('email', models.EmailField(max_length=254, verbose_name='آدرس الكترونيكي')),
                ('phone', models.CharField(max_length=20, verbose_name='تلفن')),
                ('number', models.IntegerField(verbose_name='تعداد')),
                ('date', models.DateField(verbose_name='تاريخ')),
                ('time', models.TimeField(verbose_name='ساعت')),
            ],
        ),
    ]
