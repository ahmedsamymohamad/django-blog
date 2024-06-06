# Generated by Django 4.2.5 on 2023-09-10 11:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="dislikes",
            field=models.ManyToManyField(
                blank=True, related_name="dislikes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="mage",
            field=models.ImageField(
                blank=True,
                help_text="Upload an image to accompany this post.",
                null=True,
                upload_to="post_images/",
            ),
        ),
    ]