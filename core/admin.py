from django.contrib import admin
from core.models import Post, Comment, ReplyComment, TempImage


class TempImageAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "desc"]

class PostAdmin(admin.ModelAdmin):
    list_editable = ["active"]
    list_display = ["thumbnail", "user", "title", "visibility", "active"]
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_editable = ["active"]
    list_display = ["user", "post", "comment", "active"]


class ReplyCommentAdmin(admin.ModelAdmin):
    list_editable = ["active"]
    list_display = ["user", "comment", "reply", "active"]


admin.site.register(TempImage, TempImageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ReplyComment, ReplyCommentAdmin)
