from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from users.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = RichTextUploadingField()
    thumbnail = models.ImageField(default='default/thumbnail.jpg' ,upload_to='posts/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def comment_list(self):
        return Comment.objects.filter(post=self)

    @property
    def comment_count(self):
        return self.comment_list.count()

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-timestamp']