# Generated by Django 4.0.6 on 2022-09-13 09:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blogposts', to=settings.AUTH_USER_MODEL),
        ),
    ]
