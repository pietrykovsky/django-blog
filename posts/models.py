from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from users.models import User

def post_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename=f'thumbnail.{ext}'
    return f'posts/{instance.id}/{filename}'

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
        
    @property
    def posts_count(self):
        posts = Post.objects.filter(category=self)
        return posts.count()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    content = RichTextUploadingField()
    thumbnail = models.ImageField(default='default/thumbnail.jpg' , upload_to=post_directory_path)
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