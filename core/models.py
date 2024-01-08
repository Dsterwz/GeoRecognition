import shortuuid

from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.text import slugify
from django.utils.html import format_html

from userauths.models import User, user_directory_path


VISIBILITY = (
    ("Only me", "Only me"),
    ("Everyone", "Everyone"),
)

class TempImage(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='tmp')
    desc = models.TextField(max_length=1000, blank=True, null=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    visibility = models.CharField(max_length=10, default="everyone", choices=VISIBILITY)
    pid = ShortUUIDField(
        length=7, max_length=25, alphabet="abcdefghijklmnopqrstuvxyz123"
    )
    likes = models.ManyToManyField(User, blank=True, related_name="likes")
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    views = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Post"

    def save(self, *args, **kwargs):
        uuid_key = shortuuid.uuid()
        uniqueid = uuid_key[:6]
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) + "-" + str(uniqueid.lower())
        super(Post, self).save(*args, **kwargs)

    def thumbnail(self):
        return format_html(
            '<img src="/media/{}" style="width: 50px; height: 50px; border-radius: 5px; object-fit: cover" />'.format(
                self.image
            )
        )
        # return mark_safe('<img src="/media/%s" width="50" height="50" object-fit:"cover" style="border-radius: 5px;" />' % (self.image))

    def post_comments(self):
        comments = Comment.objects.filter(post=self, active=True).order_by("-id")
        return comments


class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_user"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name="comment_likes")
    cid = ShortUUIDField(
        length=7, max_length=25, alphabet="abcdefghijklmnopqrstuvxyz123"
    )

    def __str__(self):
        return str(self.comment)

    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Comment"

    def comment_replies(self):
        comment_replies = ReplyComment.objects.filter(comment=self, active=True)
        return comment_replies


class ReplyComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reply_user")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name="reply_likes")
    cid = ShortUUIDField(
        length=7, max_length=25, alphabet="abcdefghijklmnopqrstuvxyz123"
    )

    def __str__(self):
        return str(self.comment)

    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "ReplyComment"
