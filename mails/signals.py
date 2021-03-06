from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from blog.settings import EMAIL_HOST_USER
from posts.models import Post
from .models import NewsletterSignup

# sends notification email to subscribers every time a new post is created 
@receiver(post_save, sender=Post)
def send_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'Blog name: new post created!'
        html_message = render_to_string('mail.html', {'post': instance})
        plain_message = strip_tags(html_message)
        from_email = EMAIL_HOST_USER
        to_emails = []
        for user in NewsletterSignup.objects.all():
            to_emails.append(user.email)
        
        send_mail(subject, plain_message, from_email, to_emails, html_message=html_message)


