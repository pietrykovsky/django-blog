# Generated by Django 4.0.2 on 2022-02-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='user.svg', upload_to='users/<built-in function id>/'),
        ),
    ]
