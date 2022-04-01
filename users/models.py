from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, help_text="Required.", error_messages={"unique": "A user with that email adress already exists.",},)
    avatar = models.ImageField(default='default/user.svg', upload_to='users/')
    is_redactor = models.BooleanField(default=False)