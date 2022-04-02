from django.db import models
from django.contrib.auth.models import AbstractUser

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename=f'avatar.{ext}'
    return f'users/{instance.id}/{filename}'

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, help_text="Required.", error_messages={"unique": "A user with that email adress already exists.",},)
    avatar = models.ImageField(default='default/user.svg', upload_to=user_directory_path)
    is_redactor = models.BooleanField(default=False)