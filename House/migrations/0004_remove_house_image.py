# Generated by Django 3.1.1 on 2020-09-28 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0003_house_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='image',
        ),
    ]
