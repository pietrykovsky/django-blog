# Generated by Django 4.0.2 on 2022-02-25 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_postview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
    ]