# Generated by Django 4.0.2 on 2022-02-24 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]