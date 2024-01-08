# Generated by Django 5.0 on 2023-12-29 21:46

import django.db.models.deletion
import shortuuid.django_fields
import userauths.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=userauths.models.user_directory_path,
                    ),
                ),
                (
                    "visibility",
                    models.CharField(
                        choices=[("Only me", "Only me"), ("Everyone", "Everyone")],
                        default="everyone",
                        max_length=10,
                    ),
                ),
                (
                    "pid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijklmnopqrstuvxyz123",
                        length=7,
                        max_length=25,
                        prefix="",
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("slug", models.SlugField(unique=True)),
                ("views", models.PositiveIntegerField(default=0)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Post",
                "ordering": ["-date"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.CharField(max_length=1000)),
                ("active", models.BooleanField(default=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "cid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijklmnopqrstuvxyz123",
                        length=7,
                        max_length=25,
                        prefix="",
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="comment_likes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.post"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Comment",
                "ordering": ["-date"],
            },
        ),
        migrations.CreateModel(
            name="ReplyComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reply", models.CharField(max_length=1000)),
                ("active", models.BooleanField(default=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "cid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijklmnopqrstuvxyz123",
                        length=7,
                        max_length=25,
                        prefix="",
                    ),
                ),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.comment"
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="reply_likes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reply_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "ReplyComment",
                "ordering": ["-date"],
            },
        ),
    ]
