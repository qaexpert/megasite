# Generated by Django 4.2 on 2023-04-18 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True,
                default="profile_images/default.jpg",
                null=True,
                upload_to="profile_images/",
                verbose_name="Изображение",
            ),
        ),
        migrations.AlterField(
            model_name="skill",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
