from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Q

from .forms import CommentForm
from .models import Post, Comment, PostView, Category
from users.models import User

from .decorators import user_is_redactor, user_is_comment_author


# Create your views here.
def home(request):
    posts = Post.objects.all()
    recent = posts[:3]
    popular = sorted(posts, key = lambda post: post.view_count, reverse = True)[:3]
    context = {'popular': popular, 'recent': recent}
    return render(request, 'index.html', context)

def blog(request):
    latest = Post.objects.all()[:3]
    if request.GET.get('search'):
        search = request.GET.get('search')
        post_list = Post.objects.filter(Q(title__icontains=search) | Q(content__icontains=search) | Q(category__title__icontains=search) | Q(description__icontains=search) | Q(author__username__icontains=search)).distinct() 
    else:
        post_list = Post.objects.all()
        
    category_list = Category.objects.all()
    paginator = Paginator(post_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'latest': latest, 'page_obj': page_obj, 'category_list': category_list}
    return render(request, 'blog.html', context)

@method_decorator(user_is_redactor, name="dispatch")
class CategoryCreateView(CreateView):
    model = Category
    fields = ['title']
    template_name = 'create_category.html'
    success_url = reverse_lazy('blog')

@method_decorator(user_is_redactor, name="dispatch")
class CategoryEditView(UpdateView):
    model = Category
    fields = ['title']
    template_name = 'edit_category.html'
    success_url = reverse_lazy('blog')

@login_required
@user_is_redactor
def category_delete(request, pk):
    if request.method == 'POST':
        category = get_object_or_404(Category, pk=pk)
        category.delete()
    return redirect('blog')

@method_decorator(user_is_redactor, name="dispatch")
class PostCreateView(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['category' ,'title', 'description', 'thumbnail', 'content']
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()

        return super().form_valid(form)

@method_decorator(user_is_redactor, name="dispatch")
class PostEditView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['category' ,'title', 'description','thumbnail', 'content']

    def form_valid(self, form):
        self.object = form.save()
        return redirect(reverse('post', kwargs={'pk': form.instance.pk}))

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    paginator = Paginator(post.comment_list, 10)
    page_number = request.GET.get('page')

    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=post)

    page_obj = paginator.get_page(page_number)
    latest = Post.objects.all()[:3]
    form = CommentForm(request.POST or None)
    category_list = Category.objects.all()
    context = {'post': post, 'latest': latest, 'form': form, 'page_obj': page_obj, 'category_list': category_list}

    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('post', kwargs={'pk': pk}))

    return render(request, 'post.html', context)

@login_required
@user_is_redactor
def post_delete(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
    return redirect(reverse('home'))

@login_required
@user_is_comment_author
def comment_delete(request, pk):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=pk)
        post_id = comment.post.pk
        comment.delete()
    return redirect(reverse('post', kwargs={'pk': post_id}))