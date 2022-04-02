# Generated by Django 4.0.2 on 2022-04-02 18:38

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default/thumbnail.jpg', upload_to=posts.models.post_directory_path),
        ),
    ]