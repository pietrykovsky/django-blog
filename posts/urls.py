from django.urls import path
from .views import home, blog, PostCreateView, PostEditView, post_detail_view, post_delete, comment_delete, CategoryCreateView, CategoryEditView, category_delete

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('post/<int:pk>/', post_detail_view, name='post'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('comment/<int:pk>/delete/', comment_delete, name='comment_delete'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', CategoryEditView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', category_delete, name='category_delete'),
]