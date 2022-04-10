from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from posts.decorators import user_is_redactor
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('posts.urls')),
    path('', include('mails.urls')),
    path('ckeditor/upload/', user_is_redactor(ckeditor_views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(user_is_redactor(ckeditor_views.browse)), name='ckeditor_browse'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
